# test_ingest.py

from rag.ingest import store_businesses

sample = [
    {
        "business_name":"Vels Dental",
        "phone":"9894888736",
        "trust_score":8
    }
]

store_businesses(sample)

print("Stored")