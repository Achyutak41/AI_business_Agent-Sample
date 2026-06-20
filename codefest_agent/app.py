import streamlit as st
import time
from agent import run_agent
from database import clear_cache

# ── PAGE CONFIG ──────────────────────────
st.set_page_config(
    page_title="AI Business Research Agent",
    page_icon="🔍",
    layout="wide"
)

# ── DARK THEME CSS ───────────────────────
st.markdown("""
<style>
    .stApp { background-color: #1A1A2E; color: #FFFFFF; }
    .main-title {
        font-size: 2.5rem; font-weight: 700;
        background: linear-gradient(90deg, #185FA5, #1D9E75);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center; padding: 1rem 0;
    }
    .subtitle {
        text-align: center; color: #888888;
        font-size: 1rem; margin-bottom: 2rem;
    }
    .business-card {
        background: #16213E;
        border: 1px solid #0F3460;
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
    .business-name {
        font-size: 1.1rem; font-weight: 600;
        color: #4FC3F7; margin-bottom: 0.5rem;
    }
    .info-row { color: #CCCCCC; font-size: 0.9rem; margin: 3px 0; }
    .score-high { color: #1D9E75; font-weight: 700; }
    .score-mid  { color: #E07B16; font-weight: 700; }
    .score-low  { color: #A32D2D; font-weight: 700; }
    .conflict   { color: #FF6B6B; font-size: 0.85rem; }
    .stat-box {
        background: #16213E;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        border: 1px solid #0F3460;
    }
    .stat-number {
        font-size: 2rem; font-weight: 700; color: #4FC3F7;
    }
    .stat-label { color: #888888; font-size: 0.85rem; }
    .stTextInput input {
        background: #16213E !important;
        color: white !important;
        border: 1px solid #185FA5 !important;
        border-radius: 8px !important;
        font-size: 1rem !important;
    }
    .stButton button {
        background: linear-gradient(90deg, #185FA5, #1D9E75) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        width: 100% !important;
        padding: 0.6rem !important;
    }
</style>
""", unsafe_allow_html=True)

# ── HEADER ───────────────────────────────
st.markdown('<div class="main-title">🔍 AI Business Research Agent</div>',
            unsafe_allow_html=True)
st.markdown('<div class="subtitle">Find, verify and organize business information from across the internet</div>',
            unsafe_allow_html=True)

# ── SEARCH BAR ───────────────────────────
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    query = st.text_input(
        "",
        placeholder="e.g. Cardiologists in Birmingham, Plumbers in Houston...",
        label_visibility="collapsed"
    )
    
    col_a, col_b = st.columns([3, 1])
    with col_a:
        search_btn = st.button("🔍 Search Businesses")
    with col_b:
        clear_btn = st.button("🗑 Clear Cache")

    if clear_btn and query:
        clear_cache(query)
        st.success(f"Cache cleared for: {query}")

# ── SEARCH LOGIC ─────────────────────────
if search_btn and query:
    with st.spinner("🤖 Agent is researching businesses..."):

        # Progress messages
        progress_bar = st.progress(0)
        status = st.empty()

        status.text("🔍 Checking cache...")
        progress_bar.progress(10)
        time.sleep(0.3)

        status.text("🌐 Searching multiple sources...")
        progress_bar.progress(30)

        # Run agent
        start = time.time()
        report = run_agent(query)
        elapsed = time.time() - start

        progress_bar.progress(80)
        status.text("✅ Verifying and deduplicating...")
        time.sleep(0.3)
        progress_bar.progress(100)
        status.empty()
        progress_bar.empty()

    s = report["search_summary"]
    q = report["data_quality"]
    businesses = report["businesses"]

    # ── SOURCE BADGE ─────────────────────
    if s.get("source") == "cache":
        st.success("⚡ Results from cache — instant response!")
    else:
        st.success(f"✅ Live research completed in {s['research_duration']}")

    # ── STATS ROW ────────────────────────
    st.markdown("### 📊 Research Summary")
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{s['businesses_found']}</div>
            <div class="stat-label">Found</div></div>""",
            unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{s['businesses_verified']}</div>
            <div class="stat-label">Verified</div></div>""",
            unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{s['duplicates_removed']}</div>
            <div class="stat-label">Duplicates Removed</div></div>""",
            unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{s['sources_searched']}</div>
            <div class="stat-label">Sources Searched</div></div>""",
            unsafe_allow_html=True)
    with c5:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{q['records_with_phone']}</div>
            <div class="stat-label">Have Phone</div></div>""",
            unsafe_allow_html=True)

    st.markdown("---")

    # ── RESULTS ──────────────────────────
    left, right = st.columns([2, 1])

    with left:
        st.markdown(f"### 🏢 Businesses Found ({len(businesses)})")
        for b in businesses:
            score = b.get("trust_score", 1)
            if score >= 7:
                score_class = "score-high"
            elif score >= 4:
                score_class = "score-mid"
            else:
                score_class = "score-low"

            conflicts = b.get("conflict_flags", [])
            conflict_html = ""
            if conflicts:
                conflict_html = '<div class="conflict">⚠️ Conflict detected in: ' + \
                    ", ".join([c["field"] for c in conflicts]) + '</div>'

            st.markdown(f"""
            <div class="business-card">
                <div class="business-name">🏢 {b.get('business_name','Unknown')}</div>
                <div class="info-row">📞 {b.get('phone') or 'Not found'}</div>
                <div class="info-row">📍 {b.get('address') or 'Not found'}</div>
                <div class="info-row">🌐 {b.get('website') or 'Not found'}</div>
                <div class="info-row">⭐ Rating: {b.get('rating') or 'N/A'}</div>
                <div class="info-row">🕐 {b.get('working_hours') or 'Not found'}</div>
                <div class="info-row">Trust Score: 
                    <span class="{score_class}">{score}/10</span>
                </div>
                {conflict_html}
            </div>""", unsafe_allow_html=True)

    with right:
        st.markdown("### 📈 Data Quality")
        st.metric("With Phone",   q["records_with_phone"])
        st.metric("With Address", q["records_with_address"])
        st.metric("With Website", q["records_with_website"])
        st.metric("With Rating",  q["records_with_rating"])
        st.metric("With Hours",   q["records_with_hours"])

        st.markdown("### 💾 Download")
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        import io

        def generate_pdf(report):
             buffer = io.BytesIO()
             doc = SimpleDocTemplate(buffer, pagesize=A4)
             styles = getSampleStyleSheet()
             story = []
             s = report["search_summary"]
             q = report["data_quality"]
             story.append(Paragraph("AI Business Research Agent", styles["Title"]))
             story.append(Paragraph(f"Query: {s['query']}", styles["Heading2"]))
             story.append(Spacer(1, 10))
             story.append(Paragraph("Search Summary", styles["Heading2"]))
             story.append(Paragraph(f"Businesses Found: {s['businesses_found']}", styles["Normal"]))
             story.append(Paragraph(f"Businesses Verified: {s['businesses_verified']}", styles["Normal"]))
             story.append(Paragraph(f"Duplicates Removed: {s['duplicates_removed']}", styles["Normal"]))
             story.append(Paragraph(f"Time Taken: {s['research_duration']}", styles["Normal"]))
             story.append(Spacer(1, 10))
             story.append(Paragraph("Data Quality", styles["Heading2"]))
             story.append(Paragraph(f"With Phone: {q['records_with_phone']}", styles["Normal"]))
             story.append(Paragraph(f"With Address: {q['records_with_address']}", styles["Normal"]))
             story.append(Paragraph(f"With Website: {q['records_with_website']}", styles["Normal"]))
             story.append(Spacer(1, 10))
             story.append(Paragraph("Businesses", styles["Heading2"]))

             for b in report["businesses"]:
                    story.append(Paragraph(f"Name: {b.get('business_name','N/A')}", styles["Heading3"]))
                    story.append(Paragraph(f"Phone: {b.get('phone') or 'N/A'}", styles["Normal"]))
                    story.append(Paragraph(f"Address: {b.get('address') or 'N/A'}", styles["Normal"]))
                    story.append(Paragraph(f"Website: {b.get('website') or 'N/A'}", styles["Normal"]))
                    story.append(Paragraph(f"Rating: {b.get('rating') or 'N/A'}", styles["Normal"]))
                    story.append(Paragraph(f"Trust Score: {b.get('trust_score','N/A')}/10", styles["Normal"]))
                    story.append(Spacer(1, 8))

             doc.build(story)
             buffer.seek(0)
             return buffer

        pdf_buffer = generate_pdf(report)
        st.download_button(
    label="⬇ Download PDF Report",
    data=pdf_buffer,
    file_name=f"research_{query.replace(' ','_')}.pdf",
    mime="application/pdf"
)

elif search_btn and not query:
    st.warning("Please enter a search query!")

# ── FOOTER ───────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#555555; font-size:0.8rem;'>
AI Business Research Agent • Chettinad CodeFest 2026 • 
Achyuta K & Bhuvaneshwari • SASTRA University
</div>""", unsafe_allow_html=True)