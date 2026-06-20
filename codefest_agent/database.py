from pymongo import MongoClient
from dotenv import load_dotenv
import streamlit as st
import os
from datetime import datetime, timedelta

load_dotenv()

def get_env(key):
    try:
        return st.secrets[key]
    except:
        return os.getenv(key)
def get_db():
    client = MongoClient(
        get_env("MONGO_URL"),
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    db = client[get_env("DB_NAME")]
    return db

def check_cache(query):
    db = get_db()
    cache = db["search_cache"]
    query_lower = query.lower().strip()
    result = cache.find_one({"query": query_lower})
    if result:
        # Check if cache is less than 24 hours old
        age = datetime.utcnow() - result["timestamp"]
        if age < timedelta(hours=24):
            print(f"CACHE HIT: {query}")
            return result["businesses"]
    print(f"CACHE MISS: {query}")
    return None

def save_to_cache(query, businesses):
    db = get_db()
    cache = db["search_cache"]
    query_lower = query.lower().strip()
    cache.update_one(
        {"query": query_lower},
        {"$set": {
            "query": query_lower,
            "businesses": businesses,
            "timestamp": datetime.utcnow(),
            "count": len(businesses)
        }},
        upsert=True
    )
    print(f"SAVED TO CACHE: {query} — {len(businesses)} businesses")

def save_businesses(businesses):
    db = get_db()
    collection = db["businesses"]
    if businesses:
        collection.insert_many(businesses)
        print(f"SAVED {len(businesses)} businesses to DB")

def clear_cache(query=None):
    db = get_db()
    cache = db["search_cache"]
    if query:
        cache.delete_one({"query": query.lower().strip()})
        print(f"CLEARED cache for: {query}")
    else:
        cache.delete_many({})
        print("CLEARED all cache")