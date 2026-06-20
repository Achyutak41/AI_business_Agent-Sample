from report import generate_report, save_report_json, print_summary

businesses = [
    {
        "business_name": "38th Street Dental",
        "phone": "(512) 458-6222",
        "address": "1500 W 38th St Austin TX",
        "website": "38thstreetdental.com",
        "rating": 4.5,
        "working_hours": "Mon-Fri 8am-5pm",
        "trust_score": 8,
        "conflict_flags": [],
        "source_urls": {"website": "site1.com"}
    },
    {
        "business_name": "Smiles of Austin",
        "phone": "(512) 451-8310",
        "address": None,
        "website": "smilesofaustin.com",
        "rating": None,
        "working_hours": None,
        "trust_score": 3,
        "conflict_flags": [],
        "source_urls": {"website": "site1.com"}
    },
]

report = generate_report(
    query="Dentists in Austin",
    businesses=businesses,
    duplicate_count=1,
    sources_searched=3,
    time_taken=14.5
)

print_summary(report)
filename = save_report_json(report)
print(f"\nJSON file created: {filename}")
print("\nREPORT TEST PASSED!")