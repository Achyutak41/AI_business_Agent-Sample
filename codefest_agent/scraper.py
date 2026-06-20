import requests
from bs4 import BeautifulSoup
import re
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def scrape_business(url, title="", snippet=""):
    """
    Scrape a single business URL
    Extract: name, phone, address, rating, hours, website
    """
    business = {
        "business_name": title.split("|")[0].strip(),
        "phone": None,
        "address": None,
        "website": url,
        "working_hours": None,
        "rating": None,
        "review_count": None,
        "services": [],
        "source_urls": {"website": url},
        "trust_score": 1,
        "conflict_flags": []
    }

    try:
        response = requests.get(url, headers=HEADERS, timeout=8)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(" ", strip=True)

        # Extract phone
        phone_pattern = r'(\+?1?\s?[\(\-\.]?\d{3}[\)\-\.\s]?\s?\d{3}[\-\.\s]?\d{4})'
        phones = re.findall(phone_pattern, text)
        if phones:
            business["phone"] = phones[0].strip()
            business["source_urls"]["phone"] = url
            business["trust_score"] += 2

        # Extract address
        address_pattern = r'\d+\s+[\w\s]+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Way|Circle|Cir)[,\s]+[\w\s]+[,\s]+[A-Z]{2}\s+\d{5}'
        addresses = re.findall(address_pattern, text, re.IGNORECASE)
        if addresses:
            business["address"] = addresses[0].strip()
            business["source_urls"]["address"] = url
            business["trust_score"] += 2

        # Extract rating
        rating_pattern = r'(\d+\.?\d*)\s*(?:out of\s*)?(?:\/\s*)?5\s*(?:stars?)?'
        ratings = re.findall(rating_pattern, text)
        if ratings:
            for r in ratings:
                if 1.0 <= float(r) <= 5.0:
                    business["rating"] = float(r)
                    break

        # Extract working hours
        hours_keywords = ["Monday", "Tuesday", "open", "hours", "am", "pm"]
        for keyword in hours_keywords:
            if keyword.lower() in text.lower():
                idx = text.lower().find(keyword.lower())
                hours_snippet = text[idx:idx+100]
                business["working_hours"] = hours_snippet.strip()
                business["source_urls"]["working_hours"] = url
                break

        # Extract business name from page title
        if soup.title and soup.title.string:
            page_title = soup.title.string.strip()
            if len(page_title) > 3 and len(page_title) < 100:
                business["business_name"] = page_title.split("|")[0].split("-")[0].strip()

        print(f"SCRAPED: {business['business_name'][:40]} | Phone: {business['phone']} | Score: {business['trust_score']}")

    except Exception as e:
        print(f"SCRAPE FAILED: {url[:50]} — {e}")

    return business


def scrape_all(search_results):
    """Scrape all URLs from search results"""
    businesses = []
    for result in search_results:
        url = result.get("url", "")
        title = result.get("title", "")
        snippet = result.get("snippet", "")

        # Skip non-business URLs
        skip = ["wikipedia", "reddit", "quora", "youtube", "twitter", "facebook.com/pages","yelp.com", "m.yelp.com","healthgrades.com", "zocdoc.com"]
        if any(s in url for s in skip):
            continue

        business = scrape_business(url, title, snippet)
        businesses.append(business)
        time.sleep(0.5)  # Be polite to servers

    return businesses