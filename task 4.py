import json
import time
from collections import Counter
import requests
from bs4 import BeautifulSoup
base_url = "https://quotes.toscrape.com"
Headers = {"User-Agent": "InternCircle-Project04-Scraper (educational use)"}
def scrape_quotes():
    url = base_url + "/"
    all_quotes = []
    while url:
        print(f"Fetching: {url}")
        try:
            response = requests.get(url, headers=Headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            break
        soup = BeautifulSoup(response.text, "html.parser")
        for item in soup.select("div.quote"):
            text_el = item.select_one("span.text")
            author_el = item.select_one("small.author")
            tag_els = item.select("a.tag")
            if text_el and author_el:
                all_quotes.append({
                    "text": text_el.get_text(strip=True),
                    "author": author_el.get_text(strip=True),
                    "tags": [tag.get_text(strip=True) for tag in tag_els],
                })
        next_btn = soup.select_one("li.next a")
        url = base_url + next_btn["href"] if next_btn else None
        if url:
            time.sleep(1)
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
