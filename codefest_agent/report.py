import json
from datetime import datetime

def generate_report(query, businesses, 
                    duplicate_count, sources_searched, 
                    time_taken):
    """
    Generate final research report
    """
    total = len(businesses)
    
    # Data quality metrics
    with_phone   = sum(1 for b in businesses if b.get("phone"))
    with_address = sum(1 for b in businesses if b.get("address"))
    with_website = sum(1 for b in businesses if b.get("website"))
    with_rating  = sum(1 for b in businesses if b.get("rating"))
    with_hours   = sum(1 for b in businesses if b.get("working_hours"))
    verified     = sum(1 for b in businesses if b.get("trust_score", 0) >= 5)

    def pct(n):
        return f"{round((n/total)*100)}%" if total > 0 else "0%"

    report = {
        "search_summary": {
            "query": query,
            "timestamp": datetime.utcnow().isoformat(),
            "businesses_found": total,
            "businesses_verified": verified,
            "duplicates_removed": duplicate_count,
            "sources_searched": sources_searched,
            "research_duration": f"{time_taken:.1f} seconds"
        },
        "data_quality": {
            "records_with_phone":   pct(with_phone),
            "records_with_address": pct(with_address),
            "records_with_website": pct(with_website),
            "records_with_rating":  pct(with_rating),
            "records_with_hours":   pct(with_hours),
        },
        "businesses": businesses
    }

    return report

def save_report_json(report, filename=None):
    """Save report as JSON file"""
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        query_clean = report["search_summary"]["query"].replace(" ", "_")
        filename = f"report_{query_clean}_{timestamp}.json"
    
    with open(filename, "w") as f:
        json.dump(report, f, indent=2, default=str)
    
    print(f"REPORT SAVED: {filename}")
    return filename

def print_summary(report):
    """Print report summary to console"""
    s = report["search_summary"]
    q = report["data_quality"]
    
    print("\n" + "="*50)
    print("RESEARCH REPORT SUMMARY")
    print("="*50)
    print(f"Query              : {s['query']}")
    print(f"Businesses Found   : {s['businesses_found']}")
    print(f"Businesses Verified: {s['businesses_verified']}")
    print(f"Duplicates Removed : {s['duplicates_removed']}")
    print(f"Sources Searched   : {s['sources_searched']}")
    print(f"Time Taken         : {s['research_duration']}")
    print("\nDATA QUALITY:")
    print(f"  With Phone   : {q['records_with_phone']}")
    print(f"  With Address : {q['records_with_address']}")
    print(f"  With Website : {q['records_with_website']}")
    print(f"  With Rating  : {q['records_with_rating']}")
    print(f"  With Hours   : {q['records_with_hours']}")
    print("="*50)