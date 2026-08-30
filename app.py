import streamlit as st
import os
from langchain_groq import ChatGroq

st.set_page_config(page_title="CareerPilot AI", page_icon="🚀", layout="wide")

# --- CONFIG ---
GROQ_KEY = st.secrets.get("GROQ_API_KEY") if "GROQ_API_KEY" in st.secrets else None

st.title("🚀 CareerPilot Agent")
st.caption("Agents for Humans 2026 | Groq Llama 3.3 | Nairobi")

if not GROQ_KEY:
    st.warning("⚠️ Add your Groq API Key to run")
    st.code('GROQ_API_KEY = "gsk_your_key_here"', language="toml")
    st.info("Get free key at: console.groq.com/keys → Then go to Streamlit: Manage app → Settings → Secrets")
    st.stop()

try:
    llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_KEY, temperature=0.3)
except Exception as e:
    st.error(f"Invalid Groq Key: {e}")
    st.stop()

role = st.selectbox("Target Role", ["AI Engineer","Data Scientist","Full Stack Developer","Cloud Engineer","Data Analyst"])
level = st.selectbox("Level", ["Student","Entry","Mid","Senior"])

job = st.text_area("📋 Paste Job Advert", height=200, placeholder="Paste here...")
skills = st.text_area("🧑‍💻 Your Skills / CV", height=150, placeholder="Python, SQL...")

if st.button("🚀 Generate Roadmap", type="primary", use_container_width=True):
    if not job.strip():
        st.warning("Please paste a job advert first")
        st.stop()
    
    with st.spinner("Agents analyzing..."):
        prompt = f"""You are CareerPilot multi-agent system for Kenya.
Target Role: {role}, Level: {level}
Job Advert: {job}
User Profile: {skills}

Output in clean markdown:
1. Match Score (0-100%)
2. Skill Gap
3. 30-60-90 Day Roadmap
4. 3 Resume Bullets
5. 5 Interview Questions
Be concise and encouraging."""

        try:
            response = llm.invoke(prompt)
            st.success("✅ Analysis Complete")
            st.markdown(response.content)
            st.balloons()
        except Exception as e:
            err = str(e)
            if "401" in err or "invalid_api_key" in err.lower() or "authentication" in err.lower():
                st.error("❌ Invalid GROQ_API_KEY. Check Secrets.")
                st.code("Go to: Manage app → Settings → Secrets")
            elif "429" in err or "rate" in err.lower():
                st.error("⏳ Groq rate limit. Wait 30 seconds and retry.")
            else:
                st.error(f"Groq Error: {err[:200]}")
            st.stop()

st.divider()
st.caption("Built by Wycliffe | Agents for Humans 2026")
