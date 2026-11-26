import html
import json
import re
import time
import urllib.error
import urllib.request
from collections import Counter

BASE_URL = "https://toscrape.com"
HEADERS = {"User-Agent": "InternCircle-Project04-Scraper (educational use)"}


def fetch_page(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as response:
        return response.read().decode("utf-8")


def parse_quotes(page_html):
    quotes = []
    # Split page into individual quote blocks
    blocks = page_html.split('<div class="quote"')[1:]

    for block in blocks:
        text_match = re.search(r'<span class="text"[^>]*>(.*?)</span>', block, re.S)
        author_match = re.search(r'<small class="author"[^>]*>(.*?)</small>', block, re.S)
        tag_matches = re.findall(r'<a class="tag"[^>]*>(.*?)</a>', block, re.S)

        if text_match and author_match:
            quotes.append({
                "text": html.unescape(text_match.group(1)).strip(),
                "author": html.unescape(author_match.group(1)).strip(),
                "tags": [html.unescape(t).strip() for t in tag_matches],
            })

    # Look for the "Next" page link
    next_match = re.search(r'<li class="next">\s*<a href="([^"]+)"', page_html)
    next_url = BASE_URL + next_match.group(1) if next_match else None

    return quotes, next_url


def scrape_quotes():
    url = BASE_URL + "/"
    all_quotes = []

    while url:
        print(f"Fetching: {url}")
        try:
            page_html = fetch_page(url)
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"Request failed: {e}")
            break

        page_quotes, url = parse_quotes(page_html)
        all_quotes.extend(page_quotes)

        if url:
            time.sleep(1)  # Polite delay between pages

    return all_quotes


def save_files(quotes):
    with open("quotes.json", "w", encoding="utf-8") as jf:
        json.dump(quotes, jf, indent=2, ensure_ascii=False)

    with open("quotes.txt", "w", encoding="utf-8") as tf:
        for i, q in enumerate(quotes, start=1):
            tags_str = ", ".join(q["tags"]) if q["tags"] else "None"
            tf.write(f"{i}. {q['text']}\n")
            tf.write(f"   - Author: {q['author']} | Tags: {tags_str}\n\n")


def print_summary(quotes):
    if not quotes:
        print("No quotes were scraped.")
        return

    authors = Counter(q["author"] for q in quotes)
    tags = Counter(tag for q in quotes for tag in q["tags"])

    top_author, author_count = authors.most_common(1)[0]
    top_tag, tag_count = tags.most_common(1)[0]

    print("\n--- Scraping Summary ---")
    print(f"Total quotes scraped : {len(quotes)}")
    print(f"Most quoted author   : {top_author} ({author_count} quotes)")
    print(f"Most common tag      : '{top_tag}' ({tag_count} times)")


if __name__ == "__main__":
    data = scrape_quotes()
    save_files(data)
    print_summary(data)
