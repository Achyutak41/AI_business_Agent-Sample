# 🔍 AI Business Research Agent

> An AI-powered business discovery, verification, and reporting platform that researches businesses from multiple online sources, validates information, assigns trust scores, caches results using MongoDB, and generates professional PDF reports.

🏆 Developed for **Chettinad CodeFest 2026**
👨‍💻 Team Members: **Achyuta K** & **Bhuvaneshwari**
🎓 SASTRA University

---

## 📖 Overview

Finding accurate business information online often requires browsing multiple websites, comparing details, removing duplicates, and validating data manually.

The **AI Business Research Agent** automates this process by:

* Searching businesses across multiple online sources
* Collecting and consolidating business information
* Verifying business details
* Detecting conflicts and inconsistencies
* Removing duplicate records
* Assigning trust scores
* Caching results using MongoDB
* Generating professional PDF reports
* Providing data quality analytics

The system helps users quickly identify reliable businesses while reducing the effort required for manual research.

---

## ✨ Features

### 🔎 Intelligent Business Search

Search businesses using natural language queries:

```text
Dentist in Thanjavur
Cardiologists in Birmingham
Plumbers in Houston
Restaurants in Chennai
```

The AI agent gathers information from multiple sources and presents a consolidated report.

---

### ✅ Business Verification

The platform verifies:

* Phone Numbers
* Websites
* Ratings
* Working Hours
* Business Information Consistency

Businesses with more complete and reliable data receive higher trust scores.

---

### 🎯 Trust Score Calculation

Each business receives a **Trust Score (0–10)** based on:

* Data completeness
* Verification confidence
* Information consistency
* Source reliability

Example:

```text
Trust Score: 8/10
```

---

### ⚠ Conflict Detection

The system identifies conflicting information across sources, such as:

* Different phone numbers
* Different websites
* Different working hours
* Inconsistent business details

Conflicts are highlighted to help users make informed decisions.

---

### ⚡ Smart MongoDB Caching

To improve performance and reduce unnecessary web requests, the system uses MongoDB as a caching layer.

#### Cache Workflow

1. User submits a query.
2. System checks MongoDB cache.
3. If results exist:

   * Return cached results instantly.
4. If results do not exist:

   * Perform live research.
   * Verify and process data.
   * Store results in MongoDB.
   * Return fresh results.

#### Benefits

✅ Faster response times

✅ Reduced web requests

✅ Better scalability

✅ Improved user experience

✅ Research history preservation

---

### 📊 Research Analytics Dashboard

Provides key insights including:

* Businesses Found
* Businesses Verified
* Duplicates Removed
* Sources Searched
* Research Duration
* Data Quality Statistics

---

### 📄 Professional PDF Reports

Generate downloadable reports containing:

* Search Summary
* Data Quality Analysis
* Business Listings
* Trust Scores
* Conflict Information

Perfect for research, lead generation, and business intelligence workflows.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │   User Query    │
                    └────────┬────────┘
                             │
                             ▼
                 ┌──────────────────────┐
                 │  AI Research Agent   │
                 └──────────┬───────────┘
                            │
               ┌────────────┴────────────┐
               │                         │
               ▼                         ▼
      MongoDB Cache Check        Multi-Source Search

               │                         │
       Cache Hit                     Cache Miss
               │                         │
               ▼                         ▼
      Return Results          Data Collection Pipeline
                                        │
                                        ▼
                              Verification Engine
                                        │
                                        ▼
                              Duplicate Removal
                                        │
                                        ▼
                            Trust Score Calculation
                                        │
                                        ▼
                               Store in MongoDB
                                        │
                                        ▼
                           Dashboard + PDF Report
```

---

## 🔄 Workflow

```text
User Query
     ↓
MongoDB Cache Lookup
     ↓
Cache Miss
     ↓
Search Multiple Sources
     ↓
Extract Business Information
     ↓
Verify & Validate Data
     ↓
Detect Conflicts
     ↓
Remove Duplicates
     ↓
Calculate Trust Score
     ↓
Store Results in MongoDB
     ↓
Generate Dashboard
     ↓
Export PDF Report
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* MongoDB

### Data Collection & Processing

* Requests
* BeautifulSoup
* JSON Parsing
* Multi-Source Web Scraping
* Business Verification Pipeline

### Reporting

* ReportLab

### Caching

* MongoDB Query Cache

### Libraries Used

```python
streamlit
pymongo
requests
beautifulsoup4
reportlab
json
time
io
```

---

## 📂 Project Structure

```text
AI-Business-Research-Agent/
│
├── app.py                    # Streamlit Application
├── agent.py                  # AI Research Agent
├── database.py               # MongoDB Operations
├── cache_manager.py          # Cache Handling Logic
│
├── reports/
│   └── research_report.pdf
│
├── data/
│
├── .env
├── requirements.txt
│
└── README.md
```

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-Business-Research-Agent.git

cd AI-Business-Research-Agent
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```env
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=business_research
COLLECTION_NAME=business_cache
```

---

### 5. Start MongoDB

```bash
mongod
```

---

### 6. Run Application

```bash
streamlit run app.py
```

---

## 🎯 Usage

### Step 1

Launch the Streamlit application.

### Step 2

Enter a business search query.

Example:

```text
Dentist in Thanjavur
```

### Step 3

Click:

```text
🔍 Search Businesses
```

### Step 4

The AI Agent will:

* Check MongoDB cache
* Search multiple sources
* Verify business information
* Remove duplicates
* Detect conflicts
* Calculate trust scores

### Step 5

View results in the dashboard.

### Step 6

Download the PDF report.

---

## 📊 Example Output

### Query

```text
Dentist in Thanjavur
```

### Research Summary

| Metric              | Value   |
| ------------------- | ------- |
| Businesses Found    | 10      |
| Businesses Verified | 3       |
| Duplicates Removed  | 0       |
| Time Taken          | 0.1 sec |

### Data Quality

| Metric        | Coverage |
| ------------- | -------- |
| Phone Numbers | 30%      |
| Websites      | 100%     |
| Ratings       | 30%      |
| Working Hours | 60%      |

---

## 📈 Trust Score Levels

| Score  | Meaning             |
| ------ | ------------------- |
| 8 – 10 | Highly Reliable     |
| 5 – 7  | Moderately Reliable |
| 1 – 4  | Low Confidence      |

---

## 💡 Use Cases

### Business Intelligence

Research local businesses quickly.

### Lead Generation

Generate verified business leads.

### Market Research

Analyze businesses within a specific region.

### Competitor Analysis

Discover competitors and compare business information.

### Business Directory Creation

Build verified business databases automatically.

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

## 🌍 Impact

The AI Business Research Agent reduces manual effort involved in business discovery and verification by automating:

* Business research
* Data verification
* Duplicate detection
* Trust assessment
* Report generation

This enables researchers, marketers, startups, and business analysts to obtain reliable business information in seconds instead of hours.

---

## 🔮 Future Enhancements

* Google Maps Integration
* AI-Powered Lead Scoring
* CRM Integration
* CSV / Excel Export
* Email Extraction
* Contact Validation
* Multi-language Support
* Business Categorization
* Advanced Verification Engine
* Cloud Deployment
* Real-Time Business Monitoring
* AI-Powered Recommendation System

---

## 🏆 Hackathon Details

### Event

Chettinad CodeFest 2026

### Project

AI Business Research Agent

### Theme

AI-Powered Business Intelligence & Automation

---

## 👨‍💻 Team

### Achyuta K
B.Tech Computer Science and Engineering
SASTRA University

### Bhuvaneshwari
B.Tech Computer Science and Engineering SASTRA University

---

## 📜 License

This project is developed for educational, research, and hackathon purposes.

---

## ⭐ Acknowledgements

Special thanks to:

* Chettinad CodeFest 2026
* SASTRA University
* MongoDB
* Streamlit
* ReportLab
* Open Source Python Community

---

# 🔍 AI Business Research Agent

### Find • Verify • Analyze • Report

Transforming scattered business information into reliable, actionable insights through AI-powered research and verification.
