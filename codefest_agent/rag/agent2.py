import time
from search import search_businesses
from scraper import scrape_all
from deduplicator import deduplicate
from verifier import verify_all
from report import generate_report, save_report_json
from database import check_cache, save_to_cache

# Optional RAG integration
try:
    from rag.ingest import store_businesses
    RAG_AVAILABLE = True
except Exception:
    RAG_AVAILABLE = False


def run_agent(query):
    """
    Full pipeline:
    Query → Cache Check → Search →
    Scrape → Deduplicate → Verify → Report
    """

    start_time = time.time()

    print(f"\n{'='*50}")
    print(f"AGENT STARTING: {query}")
    print(f"{'='*50}")

    # Step 1 — Check cache first
    cached = check_cache(query)

    if cached:
        print("RETURNING CACHED RESULTS")

        report = generate_report(
            query=query,
            businesses=cached,
            duplicate_count=0,
            sources_searched=0,
            time_taken=0.1
        )

        report["search_summary"]["source"] = "cache"
        return report

    # Step 2 — Search
    search_results = search_businesses(
        query,
        max_results=10
    )

    sources_searched = len(search_results)

    # Step 3 — Scrape
    businesses = scrape_all(search_results)

    # Step 4 — Deduplicate
    businesses, duplicate_count = deduplicate(
        businesses
    )

    # Step 5 — Verify
    businesses = verify_all(
        businesses
    )

    # Step 6 — Save Cache
    save_to_cache(
        query,
        businesses
    )

    # Step 7 — Store in Vector DB (RAG)
    if RAG_AVAILABLE:
        try:
            store_businesses(
                businesses
            )
            print("Stored businesses in ChromaDB")
        except Exception as e:
            print(f"RAG Storage Error: {e}")

    # Step 8 — Generate Report
    time_taken = time.time() - start_time

    report = generate_report(
        query=query,
        businesses=businesses,
        duplicate_count=duplicate_count,
        sources_searched=sources_searched,
        time_taken=time_taken
    )

    report["search_summary"]["source"] = "live"

    # Step 9 — Save JSON
    save_report_json(report)

    return report