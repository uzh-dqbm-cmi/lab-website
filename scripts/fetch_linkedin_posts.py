#!/usr/bin/env python3
"""Sync data/linkedin_posts.yaml with the lab's LinkedIn posts.

Sources, all optional and merged together:
  1. Post URLs as command-line arguments (space- or newline-separated) —
     used by the workflow_dispatch "Run workflow" box on GitHub. Adds a
     minimal entry (no text); fill in details in the PR if wanted.
  2. The SociableKIT data feed of the page (JSON) — the default source.
     Provides text, date, repost flag and a durable image URL, so posts
     arrive as complete compact cards. Override the URL with the
     SOCIABLEKIT_FEED_URL environment variable. NOTE: on SociableKIT's
     free plan the feed only updates after a manual sync in their
     dashboard (widget id 25477913, see layouts/shortcodes docs).
  3. An RSS feed via LINKEDIN_RSS_URL (legacy fallback, normally unset).

Existing entries are never overwritten: new posts are added, and existing
entries only gain fields they are missing (e.g. text arriving later from
the feed). Entries are kept sorted newest-first using the timestamp
embedded in the post ID. The file's header comment block is preserved.

Requires PyYAML (pip install pyyaml).
"""

import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

import yaml

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "linkedin_posts.yaml"
DEFAULT_SOCIABLEKIT_FEED = "https://data.accentapi.com/feed/25477913.json"

# Post URLs and URNs carry the ID as e.g. "...-activity-71234...-xYz",
# "urn:li:ugcPost:71234..." etc.
URN_RE = re.compile(r"(activity|ugcPost|share)[-:](\d{10,})")


def urn_id(urn):
    m = URN_RE.search(urn or "")
    return m.group(2) if m else None


def post_timestamp(urn):
    """LinkedIn IDs are snowflakes: the top bits are a ms timestamp."""
    pid = urn_id(urn)
    return int(pid) >> 22 if pid else 0


def month_year(iso_datetime):
    try:
        return datetime.strptime(iso_datetime[:10], "%Y-%m-%d").strftime("%B %Y")
    except (ValueError, TypeError):
        return ""


def fetch(url):
    with urllib.request.urlopen(url, timeout=30) as resp:
        return resp.read()


def entries_from_args(urls):
    for url in urls:
        m = URN_RE.search(url)
        if not m:
            print("No post ID found in: %s" % url, file=sys.stderr)
            sys.exit(1)
        yield {"urn": "urn:li:%s:%s" % m.groups()}


def entries_from_sociablekit(feed_url):
    data = json.loads(fetch(feed_url))
    for p in data.get("posts", []):
        m = URN_RE.search(p.get("post_url") or "")
        if not m:
            continue
        entry = {"urn": "urn:li:%s:%s" % m.groups()}
        if str(p.get("reposted")) == "1":
            entry["label"] = "Reposted by KrauthammerLab"
        else:
            entry["author"] = "KrauthammerLab"
        date = month_year(p.get("post_date_time") or "")
        if date:
            entry["date"] = date
        text = (p.get("raw_text") or p.get("description_raw") or "").strip()
        if text:
            entry["text"] = text
        images = p.get("image_urls") or []
        image = images[0] if images else (p.get("thumbnail_url") or "")
        if image:
            entry["image"] = image
        yield entry


def entries_from_rss(feed_url):
    root = ET.fromstring(fetch(feed_url))
    for item in root.iter("item"):
        m = URN_RE.search((item.findtext("link") or "").strip())
        if m:
            yield {"urn": "urn:li:%s:%s" % m.groups()}


def str_presenter(dumper, value):
    if "\n" in value:
        # Literal blocks cannot hold trailing spaces on a line.
        value = "\n".join(line.rstrip() for line in value.splitlines())
        return dumper.represent_scalar("tag:yaml.org,2002:str", value, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", value)


yaml.add_representer(str, str_presenter)


def main():
    raw = DATA_FILE.read_text()
    header, marker, _ = raw.partition("\nposts:")
    if not marker:
        print("Could not find 'posts:' key in data file.", file=sys.stderr)
        return 1
    existing = yaml.safe_load(raw).get("posts") or []
    by_id = {}
    for e in existing:
        pid = urn_id(e.get("urn") or e.get("src") or "")
        if pid:
            by_id[pid] = e

    incoming = []
    incoming.extend(entries_from_args(" ".join(sys.argv[1:]).split()))
    feed_url = os.environ.get("SOCIABLEKIT_FEED_URL", DEFAULT_SOCIABLEKIT_FEED)
    if feed_url:
        try:
            incoming.extend(entries_from_sociablekit(feed_url))
        except Exception as exc:  # a broken feed must not kill URL mode
            print("SociableKIT feed failed: %s" % exc, file=sys.stderr)
    if os.environ.get("LINKEDIN_RSS_URL"):
        incoming.extend(entries_from_rss(os.environ["LINKEDIN_RSS_URL"]))

    added = updated = 0
    for entry in incoming:
        pid = urn_id(entry["urn"])
        current = by_id.get(pid)
        if current is None:
            by_id[pid] = entry
            added += 1
        else:
            # Only fill fields the existing entry is missing — manual
            # edits (labels, tuned heights, curated text) always win.
            missing = {k: v for k, v in entry.items() if not current.get(k)}
            if missing:
                current.update(missing)
                updated += 1

    if not added and not updated:
        print("No new LinkedIn posts found.")
        return 0

    merged = sorted(by_id.values(), key=lambda e: post_timestamp(e.get("urn") or e.get("src") or ""), reverse=True)
    body = yaml.dump({"posts": merged}, allow_unicode=True, sort_keys=False, width=1000, default_flow_style=False)
    DATA_FILE.write_text(header + "\n" + body)
    print("Added %d and updated %d post(s) in %s." % (added, updated, DATA_FILE.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
