# 🔍 AI Business Research Agent

> An AI-powered business discovery, verification, and reporting platform that researches businesses from multiple online sources, validates information, assigns trust scores, caches results using MongoDB, and generates professional PDF reports.

<div align="center">

🏆 **Chettinad CodeFest 2026 — Finals**  
👨‍💻 **Team_name:**  NexoByte   
👨‍💻 **Team_members:** Achyuta k, Bhuvaneshwari D  
🎓 **SASTRA Deemed University, Thanjavur**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://intelligent-business-agent-codefest.streamlit.app)

</div>

---

## 📖 Overview

Finding accurate business information online often requires browsing multiple websites, comparing details, removing duplicates, and validating data manually.

The **AI Business Research Agent** automates this entire process by:

* Searching businesses across multiple online sources using DuckDuckGo
* Collecting and consolidating business information via BeautifulSoup scraping
* Verifying business details across multiple sources
* Detecting conflicts and inconsistencies automatically
* Removing duplicate records using phone + address matching
* Assigning trust scores (1–10) based on data completeness
* Caching results using MongoDB Atlas for instant repeat queries
* Generating professional downloadable PDF reports
* Providing real-time data quality analytics dashboard

The system helps users quickly identify reliable businesses while reducing hours of manual research into seconds.

---

## ✨ Features

### 🔎 Intelligent Business Search

Search businesses using natural language queries in any language:

```text
Dentist in Thanjavur
Cardiologists in Birmingham
Plumbers in Houston
Restaurants in Chennai
Family Lawyers in Chicago
```

The AI agent gathers information from multiple sources and presents a consolidated verified report.

---

### ✅ Business Verification

The platform verifies:

* Phone Numbers — cross-checked across sources
* Websites — validated for accessibility
* Ratings — extracted and normalized
* Working Hours — parsed from business pages
* Business Information Consistency — flagged when conflicting

Businesses with more complete and reliable data receive higher trust scores.

---

### 🎯 Trust Score Calculation

Each business receives a **Trust Score (1–10)** based on:

| Factor | Points |
|--------|--------|
| Phone number found | +2 |
| Address found | +2 |
| Website available | +1 |
| Rating available | +1 |
| Working hours found | +1 |
| Email found | +1 |
| Multiple sources confirmed | +1 |
| Conflict detected | -1 per conflict |

```text
Trust Score 8–10 → Highly Reliable
Trust Score 5–7  → Moderately Reliable
Trust Score 1–4  → Low Confidence
```

---

### ⚠ Conflict Detection

The system identifies conflicting information across sources:

* Different phone numbers from different directories
* Inconsistent business names across listings
* Conflicting working hours

All conflicts are highlighted with ⚠️ warnings in the dashboard so users can make informed decisions.

---

### ⚡ Smart MongoDB Caching

To improve performance and reduce unnecessary web requests, the system uses **MongoDB Atlas** as a caching layer.

#### Cache Workflow

```text
User Query
    ↓
Check MongoDB Atlas Cache
    ↓
Cache HIT  ──→  Return results in < 2 seconds
    ↓
Cache MISS ──→  Live scraping pipeline
                    ↓
               Verify + Deduplicate
                    ↓
               Store in MongoDB
                    ↓
               Return fresh results
```

#### Benefits

✅ Repeat queries answered in under 2 seconds

✅ Zero redundant web requests

✅ Research history preserved across sessions

✅ Works offline for cached queries

✅ 24-hour cache expiry for fresh data

---

### 📊 Research Analytics Dashboard

Real-time insights including:

* Businesses Found
* Businesses Verified (Trust Score ≥ 5)
* Duplicates Removed
* Sources Searched
* Research Duration
* Data Quality Statistics (% with phone, address, website, rating, hours)

---

### 📄 Professional PDF Reports

Generate downloadable PDF reports containing:

* Search Summary with all metrics
* Data Quality Analysis
* Complete Business Listings
* Trust Scores per business
* Conflict flags and warnings
* SASTRA University + CodeFest branding

---

## 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │   User Query    │
                    │  (Any Language) │
                    └────────┬────────┘
                             │
                             ▼
                 ┌──────────────────────┐
                 │   AI Research Agent  │
                 │      agent.py        │
                 └──────────┬───────────┘
                            │
               ┌────────────┴────────────┐
               │                         │
               ▼                         ▼
    MongoDB Cache Check          Multi-Source Search
      database.py                   search.py
               │                         │
          Cache HIT               Cache MISS
               │                         │
               ▼                         ▼
      Return Results         scraper.py (BeautifulSoup)
      in < 2 seconds                     │
                                         ▼
                              deduplicator.py
                              (Phone + Address Match)
                                         │
                                         ▼
                                   verifier.py
                                (Trust Score 1-10)
                                         │
                                         ▼
                               Store in MongoDB
                                         │
                                         ▼
                           Streamlit Dashboard + PDF
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend UI | Streamlit |
| Backend Agent | Python 3.13 |
| Search Engine | DuckDuckGo Search (ddgs) |
| Web Scraping | BeautifulSoup4 + Requests |
| Database / Cache | MongoDB Atlas (Free Tier) |
| PDF Generation | ReportLab |
| Deduplication | difflib SequenceMatcher |
| Environment | python-dotenv |

---

## 📂 Project Structure

```text
codefest_agent/
│
├── app.py                # Streamlit UI — dark themed dashboard
├── agent.py              # Main pipeline — connects all modules
├── search.py             # DuckDuckGo multi-source search
├── scraper.py            # BeautifulSoup business data extractor
├── deduplicator.py       # Phone + address duplicate detection
├── verifier.py           # Trust score calculator
├── database.py           # MongoDB Atlas cache operations
├── report.py             # JSON + PDF report generator
│
├── requirements.txt      # All dependencies
├── .env                  # Environment variables (not committed)
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/Achyutak41/AI_business_Agent-Sample.git
cd AI_business_Agent-Sample
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Run Application

```bash
streamlit run app.py
```

---

## 🎯 Usage

### Step 1
Launch the Streamlit application at `http://localhost:8501`

### Step 2
Enter any business search query — e.g. `Dentist in Thanjavur`

### Step 3
Click **🔍 Search Businesses**

### Step 4
The AI Agent will automatically:
* Check MongoDB cache first
* Search DuckDuckGo for business URLs
* Scrape each URL for business details
* Remove duplicate businesses
* Detect conflicting information
* Calculate trust scores
* Store results in MongoDB

### Step 5
View verified business cards with trust scores in the dashboard

### Step 6
Download the PDF report using **⬇ Download PDF Report**

---

## 📊 Example Output

### Query: `Dentist in Thanjavur`

| Metric | Value |
|--------|-------|
| Businesses Found | 10 |
| Businesses Verified | 8 |
| Duplicates Removed | 1 |
| Sources Searched | 15 |
| Time Taken | 31 sec (live) / 0.1 sec (cache) |

### Data Quality

| Metric | Coverage |
|--------|----------|
| Phone Numbers | 80% |
| Websites | 100% |
| Ratings | 50% |
| Working Hours | 60% |

---
---

## 📸 Screenshots

### 🏠 Home Dashboard

Displays the search interface where users enter business queries.

![Home Dashboard](/codefest_agent/Screenshots/UI_1.png)

---

### 🔍 Business Search Results

Shows verified businesses, trust scores, ratings, contact details, and working hours.

![Search Results](/codefest_agent/Screenshots/UI_2.png)

---

### 📊 Research Analytics Dashboard

Provides insights into:

- Businesses Found
- Businesses Verified
- Duplicates Removed
- Sources Searched
- Data Quality Metrics

![Analytics Dashboard](/codefest_agent/Screenshots/UI_3.png)

---


### 📄 PDF Report Generation

Generated business research report available for download.

![PDF Report](/codefest_agent/Screenshots/sample_pdf.png)

---
## 💡 Use Cases

| Use Case | Description |
|----------|-------------|
| Business Intelligence | Research local businesses quickly |
| Lead Generation | Generate verified business contact lists |
| Market Research | Analyze businesses in a specific region |
| Competitor Analysis | Discover and compare competitor information |
| Business Directory | Build verified business databases automatically |

---

## 🔮 Future Enhancements

* Google Maps API Integration
* AI-Powered Lead Scoring
* CSV / Excel Export
* Email Extraction & Validation
* Multi-language Query Support
* Real-Time Business Monitoring
* CRM Integration
* Advanced Conflict Resolution Engine

---

## 🏆 Hackathon Details

| Detail | Info |
|--------|------|
| Event | Chettinad CodeFest 2026 |
| Round | Finals — Direct Shortlist |
| Domain | Intelligent Business Systems |
| Organizer | Overseas Cyber Technical Services Pvt. Ltd., Karaikudi |
| Project | AI Business Research Agent |

---
## 👨‍💻 Team

<div align="center">

🤝 **Team NexoByte — SASTRA Deemed University, Thanjavur**

| | |
|:---:|:---:|
| 🧑‍💻 **Achyuta K** | 👩‍💻 **Bhuvaneshwari** |
| B.Tech CSE | B.Tech CSE |
| SASTRA Deemed University | SASTRA Deemed University |
| [![GitHub](https://img.shields.io/badge/GitHub-Achyutak41-181717?style=flat&logo=github&logoColor=white)](https://github.com/Achyutak41) | [![GitHub](https://img.shields.io/badge/GitHub-BhuvaneshwariDhanabal-181717?style=flat&logo=github&logoColor=white)](https://github.com/Bhuvaneshwari-Dhanabal) |
| [![LinkedIn](https://img.shields.io/badge/LinkedIn-achyutak41-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/achyutak41) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-bhuvaneshwarid48-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bhuvaneshwarid48/) |

</div>

---  
## ⭐ Acknowledgements

* Chettinad CodeFest 2026 — OCTS Pvt. Ltd.
* SASTRA Deemed University
* MongoDB Atlas — Free cloud database
* Streamlit — Rapid UI development
* DuckDuckGo — Free search API
* ReportLab — PDF generation
* Open Source Python Community

---

# 🔍 AI Business Research Agent

### Find • Verify • Deduplicate • Score • Report

*Transforming scattered business information into reliable, actionable intelligence through AI-powered research and verification.*