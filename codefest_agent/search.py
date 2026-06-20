from ddgs import DDGS
import time

def search_businesses(query, max_results=10):
    """
    Takes a query like 'Dentists in Austin'
    Returns list of URLs to scrape
    """
    print(f"SEARCHING: {query}")
    urls = []
    
    try:
        with DDGS() as ddgs:
            # Search 1 — Direct business search
            results = ddgs.text(
                f"{query} business phone address",
                max_results=max_results
            )
            for r in results:
                urls.append({
                    "url": r["href"],
                    "title": r["title"],
                    "snippet": r["body"]
                })
            
            time.sleep(1)  # Avoid rate limiting
            
            # Search 2 — Directory search
            results2 = ddgs.text(
                f"{query} site:yelp.com OR site:yellowpages.com",
                max_results=5
            )
            for r in results2:
                urls.append({
                    "url": r["href"],
                    "title": r["title"],
                    "snippet": r["body"]
                })

    except Exception as e:
        print(f"Search error: {e}")
    
    print(f"FOUND {len(urls)} URLs for: {query}")
    return urls


def extract_basic_info_from_snippets(search_results, query):
    """
    Extract basic business info directly from
    search snippets — no scraping needed!
    """
    businesses = []
    
    for result in search_results:
        snippet = result.get("snippet", "")
        title = result.get("title", "")
        url = result.get("url", "")
        
        # Skip non-business URLs
        skip_domains = ["wikipedia", "reddit", "quora", "youtube"]
        if any(skip in url for skip in skip_domains):
            continue
        
        business = {
            "business_name": title.split("|")[0].strip(),
            "website": url,
            "snippet": snippet,
            "source_urls": {"website": url},
            "trust_score": 1
        }
        businesses.append(business)
    
    return businesses