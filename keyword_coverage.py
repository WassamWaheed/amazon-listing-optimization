import csv
import sys

def normalize(text):
    return " ".join((text or "").lower().split())

if len(sys.argv) != 2:
    print("Usage: python keyword_coverage.py sample_listing.csv")
    raise SystemExit(1)

with open(sys.argv[1], newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        listing_copy = normalize(" ".join([
            row.get("title", ""),
            row.get("bullet_1", ""),
            row.get("bullet_2", "")
        ]))

        keywords = [
            keyword.strip()
            for keyword in row.get("keywords", "").split(",")
            if keyword.strip()
        ]

        missing = [
            keyword for keyword in keywords
            if normalize(keyword) not in listing_copy
        ]

        print(f"{row['sku']}: missing keywords -> {missing if missing else 'none'}")
