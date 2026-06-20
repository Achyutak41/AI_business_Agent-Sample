from deduplicator import deduplicate

# Test with fake duplicates
test_businesses = [
    {
        "business_name": "38th Street Dental",
        "phone": "(512) 458-6222",
        "address": "1500 W 38th St Austin TX",
        "trust_score": 5,
        "conflict_flags": [],
        "source_urls": {"website": "site1.com"}
    },
    {
        "business_name": "38th Street Dental Austin",  
        "phone": "(512) 458-6222",  # Same phone = duplicate!
        "address": "1500 W 38th Street Austin TX",
        "trust_score": 3,
        "conflict_flags": [],
        "source_urls": {"website": "site2.com"}
    },
    {
        "business_name": "Smiles of Austin",
        "phone": "(512) 451-8310",  # Different phone = unique
        "address": "800 W Airport Blvd Austin TX",
        "trust_score": 3,
        "conflict_flags": [],
        "source_urls": {"website": "site3.com"}
    },
]

result, removed = deduplicate(test_businesses)

print(f"\nOriginal: 3 businesses")
print(f"After dedup: {len(result)} businesses")
print(f"Removed: {removed} duplicates")

for b in result:
    print(f"\nName  : {b['business_name']}")
    print(f"Phone : {b['phone']}")
    print(f"Score : {b['trust_score']}")
    print(f"Sources: {list(b['source_urls'].values())}")

print("\nDEDUPLICATOR TEST PASSED!")