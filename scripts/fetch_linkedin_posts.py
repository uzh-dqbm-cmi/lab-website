#!/usr/bin/env python3
"""Add new LinkedIn posts to data/linkedin_posts.yaml.

Two ways to supply posts:
  1. Post URLs as command-line arguments (space- or newline-separated) —
     used by the workflow_dispatch "Run workflow" box on GitHub. Anything
     containing an activity ID works, e.g.
     https://www.linkedin.com/posts/krauthammerlab_..._activity-7421...-QEk-
  2. An RSS feed of the page via the LINKEDIN_RSS_URL environment variable
     (optional GitHub Actions secret; only if the lab subscribes to a feed
     service such as rss.app). The feed is only used to *discover* post IDs —
     the website renders LinkedIn's official embeds, so nothing on the site
     depends on the feed service.

New entries are inserted as text right below the `posts:` line so the file's
comments and formatting are preserved. Exits 0 whether or not anything changed;
the workflow opens a PR only if the file was modified.

Stdlib only — no pip install needed.
"""

import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "linkedin_posts.yaml"
# Post URLs carry the ID as e.g. "...-activity-71234...-xYz" or
# "...-ugcPost-71234...-xYz"; embed URNs use the same type names.
ACTIVITY_RE = re.compile(r"(activity|ugcPost|share)[-:](\d{10,})")


def feed_items(url):
    with urllib.request.urlopen(url, timeout=30) as resp:
        root = ET.fromstring(resp.read())
    for item in root.iter("item"):
        yield {
            "link": (item.findtext("link") or "").strip(),
            "title": (item.findtext("title") or "").strip(),
            "pubdate": (item.findtext("pubDate") or "").strip(),
        }


def note_for(item):
    title = re.sub(r"\s+", " ", item["title"]).replace('"', "'")
    if len(title) > 70:
        title = title[:67] + "..."
    date = ""
    try:
        date = parsedate_to_datetime(item["pubdate"]).strftime(" (%Y-%m)")
    except (ValueError, TypeError):
        pass
    return f"{title}{date}" if title else date.strip(" ()")


def main():
    urls_arg = " ".join(sys.argv[1:]).split()
    feed_url = os.environ.get("LINKEDIN_RSS_URL")
    if not urls_arg and not feed_url:
        print("No post URLs given and LINKEDIN_RSS_URL is not set; nothing to do.")
        return 0

    text = DATA_FILE.read_text()
    existing = set(re.findall(r"urn:li:\w+:(\d+)", text))

    new_entries = []

    for url in urls_arg:
        m = ACTIVITY_RE.search(url)
        if not m:
            print(f"No post ID found in: {url}", file=sys.stderr)
            return 1
        kind, post_id = m.groups()
        if post_id in existing:
            print(f"Already listed: urn:li:{kind}:{post_id}")
            continue
        existing.add(post_id)
        new_entries.append(f'  - urn: "urn:li:{kind}:{post_id}"\n')

    for item in feed_items(feed_url) if feed_url else []:
        m = ACTIVITY_RE.search(item["link"])
        if not m or m.group(2) in existing:
            continue
        kind, post_id = m.groups()
        existing.add(post_id)
        entry = f'  - urn: "urn:li:{kind}:{post_id}"\n'
        note = note_for(item)
        if note:
            entry += f'    note: "{note}"\n'
        new_entries.append(entry)

    if not new_entries:
        print("No new LinkedIn posts found.")
        return 0

    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("posts:"):
            lines[i + 1 : i + 1] = new_entries
            break
    else:
        print("Could not find 'posts:' key in data file.", file=sys.stderr)
        return 1

    DATA_FILE.write_text("".join(lines))
    print(f"Added {len(new_entries)} new post(s) to {DATA_FILE.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
