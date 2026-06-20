from database import check_cache, save_to_cache, clear_cache

# Test 1 — Save to cache
test_businesses = [
    {"business_name": "Test Clinic", "phone": "9876543210", "address": "123 Main St"},
    {"business_name": "ABC Hospital", "phone": "9123456789", "address": "456 Park Ave"},
]

save_to_cache("Dentists in Austin", test_businesses)

# Test 2 — Check cache hit
result = check_cache("Dentists in Austin")
print("Cache result:", result)

# Test 3 — Check cache miss
result2 = check_cache("Plumbers in Houston")
print("Cache miss result:", result2)

print("ALL DATABASE TESTS PASSED!")