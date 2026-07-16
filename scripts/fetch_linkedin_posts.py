#!/usr/bin/env python3
"""Check an RSS feed of the lab's LinkedIn page for new posts and prepend
them to data/linkedin_posts.yaml.

The feed URL comes from the LINKEDIN_RSS_URL environment variable (a GitHub
Actions secret; e.g. an rss.app feed for linkedin.com/company/krauthammerlab).
The feed is only used to *discover* post IDs — the website renders LinkedIn's
official embeds, so nothing on the site depends on the feed service.

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
ACTIVITY_RE = re.compile(r"activity[-:](\d{10,})")


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
    url = os.environ.get("LINKEDIN_RSS_URL")
    if not url:
        print("LINKEDIN_RSS_URL is not set; nothing to do.")
        return 0

    text = DATA_FILE.read_text()
    existing = set(re.findall(r"urn:li:\w+:(\d+)", text))

    new_entries = []
    for item in feed_items(url):
        m = ACTIVITY_RE.search(item["link"])
        if not m or m.group(1) in existing:
            continue
        existing.add(m.group(1))
        entry = f'  - urn: "urn:li:activity:{m.group(1)}"\n'
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
