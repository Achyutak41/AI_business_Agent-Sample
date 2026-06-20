from difflib import SequenceMatcher

def similarity(a, b):
    """Check how similar two strings are — returns 0 to 1"""
    if not a or not b:
        return 0
    return SequenceMatcher(None, 
        a.lower().strip(), 
        b.lower().strip()
    ).ratio()

def clean_phone(phone):
    """Remove all non-numeric characters from phone"""
    if not phone:
        return None
    return ''.join(filter(str.isdigit, phone))

def are_duplicates(b1, b2):
    """
    Check if two businesses are the same
    Priority: phone match → address match → name match
    """
    # Rule 1 — Same phone = definitely same business
    phone1 = clean_phone(b1.get("phone"))
    phone2 = clean_phone(b2.get("phone"))
    if phone1 and phone2 and phone1 == phone2:
        return True, "phone_match"

    # Rule 2 — Very similar address = likely same business
    addr1 = b1.get("address", "")
    addr2 = b2.get("address", "")
    if addr1 and addr2 and similarity(addr1, addr2) > 0.85:
        return True, "address_match"

    # Rule 3 — Very similar name + same city = same business
    name1 = b1.get("business_name", "")
    name2 = b2.get("business_name", "")
    if name1 and name2 and similarity(name1, name2) > 0.90:
        return True, "name_match"

    return False, None

def merge_businesses(b1, b2):
    """
    Merge two duplicate businesses into one enriched record
    Keep the best data from each
    """
    merged = b1.copy()

    # Fill missing fields from b2
    for field in ["phone", "address", "rating", 
                  "working_hours", "email", "website"]:
        if not merged.get(field) and b2.get(field):
            merged[field] = b2[field]

    # Add conflict flags if phone differs
    if (b1.get("phone") and b2.get("phone") and 
        clean_phone(b1["phone"]) != clean_phone(b2["phone"])):
        merged["conflict_flags"].append({
            "field": "phone",
            "value1": b1["phone"],
            "value2": b2["phone"],
            "source1": b1.get("website"),
            "source2": b2.get("website")
        })

    # Increase trust score for confirmed duplicate
    merged["trust_score"] = min(10, 
        b1.get("trust_score", 1) + b2.get("trust_score", 1))

    # Merge source URLs
    merged["source_urls"].update(b2.get("source_urls", {}))

    return merged

def deduplicate(businesses):
    """
    Remove duplicate businesses from list
    Returns clean deduplicated list
    """
    if not businesses:
        return []

    unique = []
    duplicate_count = 0

    for business in businesses:
        is_dup = False
        for i, existing in enumerate(unique):
            dup, reason = are_duplicates(business, existing)
            if dup:
                print(f"DUPLICATE FOUND ({reason}): "
                      f"{business['business_name'][:30]} "
                      f"== {existing['business_name'][:30]}")
                unique[i] = merge_businesses(existing, business)
                duplicate_count += 1
                is_dup = True
                break

        if not is_dup:
            unique.append(business)

    print(f"DEDUPLICATION: {len(businesses)} → {len(unique)} "
          f"({duplicate_count} duplicates removed)")
    return unique, duplicate_count