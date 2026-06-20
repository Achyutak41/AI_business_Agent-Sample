from search import search_businesses, extract_basic_info_from_snippets

# Test search
query = "Dentists in Austin"
results = search_businesses(query, max_results=5)

print(f"\nTotal URLs found: {len(results)}")
for i, r in enumerate(results):
    print(f"{i+1}. {r['title'][:50]} → {r['url'][:60]}")

# Test extraction
businesses = extract_basic_info_from_snippets(results, query)
print(f"\nBusinesses extracted: {len(businesses)}")
for b in businesses:
    print(f"  → {b['business_name'][:40]}")

print("\nSEARCH TEST PASSED!")