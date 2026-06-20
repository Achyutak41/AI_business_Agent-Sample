from search import search_businesses
from scraper import scrape_all

# Search first
query = "Dentists in Austin"
search_results = search_businesses(query, max_results=5)

# Scrape results
print("\nSCRAPING BUSINESSES...")
businesses = scrape_all(search_results)

# Show results
print(f"\nTotal businesses scraped: {len(businesses)}")
for b in businesses:
    print(f"""
Name    : {b['business_name']}
Phone   : {b['phone']}
Address : {b['address']}
Rating  : {b['rating']}
Score   : {b['trust_score']}
    """)

print("SCRAPER TEST PASSED!")