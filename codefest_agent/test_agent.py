from agent import run_agent
from database import clear_cache

# Clear cache first to force live scraping
clear_cache("Dentists in Austin")

# Now run live
report = run_agent("Dentists in Austin")

s = report["search_summary"]
print(f"\nFINAL RESULT:")
print(f"Found    : {s['businesses_found']} businesses")
print(f"Verified : {s['businesses_verified']}")
print(f"Time     : {s['research_duration']}")
print(f"Source   : {s['source']}")

print("\nAGENT TEST PASSED!")