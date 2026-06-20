def assign_trust_score(business):
    """
    Calculate trust score 1-10 based on
    how much verified data we have
    """
    score = 0
    flags = business.get("conflict_flags", [])

    # Add points for each verified field
    if business.get("phone"):       score += 2
    if business.get("address"):     score += 2
    if business.get("website"):     score += 1
    if business.get("rating"):      score += 1
    if business.get("working_hours"): score += 1
    if business.get("email"):       score += 1
    if business.get("services"):    score += 1
    if len(business.get("source_urls", {})) >= 2: score += 1

    # Reduce score for conflicts
    score -= len(flags)

    # Cap between 1 and 10
    business["trust_score"] = max(1, min(10, score))
    return business

def verify_all(businesses):
    """Verify and score all businesses"""
    verified = []
    for b in businesses:
        b = assign_trust_score(b)
        verified.append(b)

    # Sort by trust score highest first
    verified.sort(key=lambda x: x["trust_score"], reverse=True)
    print(f"VERIFIED {len(verified)} businesses")
    return verified