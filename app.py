
import streamlit as st
import os

st.set_page_config(page_title="CareerPilot AI", page_icon="🚀", layout="wide")

# --- GET GROQ KEY ---
try:
    GROQ_KEY = st.secrets["GROQ_API_KEY"]
except:
    GROQ_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_KEY:
    st.error("❌ Add GROQ_API_KEY in Streamlit Secrets: Manage app → Settings → Secrets → GROQ_API_KEY='gsk_...'")
    st.stop()

# --- GROQ LLM ---
from langchain_groq import ChatGroq
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_KEY, temperature=0.3)

st.title("🚀 CareerPilot AI - Career Guidance Agent")
st.caption("Powered by Groq Llama 3.3 70B - No AWS needed")

col1, col2 = st.columns(2)

with col1:
    target_role = st.selectbox("Target Role", ["AI Engineer", "Data Scientist", "Full Stack Developer", "Cloud Engineer", "Data Analyst", "Product Manager", "DevOps Engineer", "Cybersecurity Analyst"])
    job_desc = st.text_area("📋 Paste Job Description", height=250, placeholder="Paste full job advert here...")

with col2:
    user_skills = st.text_area("🧑‍💻 Your Skills / Resume Summary", height=250, placeholder="Eg: Python, SQL, ML, 2 years experience...")
    exp_level = st.selectbox("Experience", ["Student", "Entry Level", "Mid Level", "Senior"])

if st.button("🚀 Generate Career Roadmap", type="primary", use_container_width=True):
    if not job_desc:
        st.warning("Paste job description first!")
    else:
        with st.spinner("Agents analyzing..."):
            prompt = f"""
            You are CareerPilot multi-agent system with 4 experts:
            1. Role Analyst, 2. Skill Gap Analyzer, 3. Roadmap Architect, 4. Coach
            
            Target Role: {target_role}
            Experience: {exp_level}
            Job Description: {job_desc}
            User Skills: {user_skills}

            Provide structured output:
            ### 1. Match Score & Summary
            ### 2. Skill Gap Analysis (Have vs Missing)
            ### 3. 30-60-90 Day Personalized Roadmap
            ### 4. Resume Bullet Rewrites (3 points tailored to this job)
            ### 5. Interview Questions to Prepare

            Be concise, practical, for hackathon judges.
            """
            try:
                response = llm.invoke(prompt).content
                st.success("✅ Analysis Complete")
                st.markdown(response)
                st.balloons()
            except Exception as e:
                st.error(f"Groq Error: {e}")

st.divider()
st.info("💡 Secrets format: GROQ_API_KEY='gsk_...' | Get key: console.groq.com/keys")
