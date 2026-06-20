from verifier import verify_all

businesses = [
    {
        "business_name": "38th Street Dental",
        "phone": "(512) 458-6222",
        "address": "1500 W 38th St Austin TX",
        "website": "38thstreetdental.com",
        "rating": 4.5,
        "working_hours": "Mon-Fri 8am-5pm",
        "trust_score": 1,
        "conflict_flags": [],
        "source_urls": {
            "website": "site1.com",
            "phone": "site2.com"
        }
    },
    {
        "business_name": "Smiles of Austin",
        "phone": "(512) 451-8310",
        "address": None,
        "website": "smilesofaustin.com",
        "rating": None,
        "working_hours": None,
        "trust_score": 1,
        "conflict_flags": [],
        "source_urls": {"website": "site1.com"}
    },
]

result = verify_all(businesses)

for b in result:
    print(f"\nName  : {b['business_name']}")
    print(f"Score : {b['trust_score']}/10")
    print(f"Flags : {b['conflict_flags']}")

print("\nVERIFIER TEST PASSED!")