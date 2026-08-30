import streamlit as st
from langchain_groq import ChatGroq

st.set_page_config(page_title="CareerPilot AI", page_icon="🚀", layout="wide")

GROQ_KEY = st.secrets.get("GROQ_API_KEY") if "GROQ_API_KEY" in st.secrets else None

st.title("🚀 CareerPilot Agent")
st.caption("Agents for Humans 2026 | Groq | Nairobi")

if not GROQ_KEY:
    st.warning("⚠️ Add GROQ_API_KEY in Secrets")
    st.code('GROQ_API_KEY = "gsk_your_key"', language="toml")
    st.stop()

# FIXED MODEL NAME - WORKING 100%
try:
    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_KEY, temperature=0.3)
except Exception as e:
    st.error(f"Key Error: {e}")
    st.stop()

role = st.selectbox("Target Role", ["AI Engineer","Data Scientist","Full Stack Developer","Cloud Engineer","Data Analyst"])
level = st.selectbox("Level", ["Student","Entry","Mid","Senior"])

job = st.text_area("📋 Paste Job Advert", height=200)
skills = st.text_area("🧑‍💻 Your Skills / CV", height=150)

if st.button("🚀 Generate Roadmap", type="primary", use_container_width=True):
    if not job.strip():
        st.warning("Paste job advert")
        st.stop()
    
    with st.spinner("Agents analyzing..."):
        prompt = f"""You are CareerPilot AI for Kenya.
Role: {role}, Level: {level}
Job: {job}
User: {skills}

Output:
1. Match Score %
2. Skill Gap
3. 30-60-90 Day Roadmap
4. 3 Resume Bullets
5. 5 Interview Qs
Keep concise."""

        try:
            response = llm.invoke(prompt)
            st.success("✅ Done")
            st.markdown(response.content)
            st.balloons()
        except Exception as e:
            st.error(f"Error: {str(e)[:300]}")
            st.stop()

st.divider()
st.caption("Built by Wycliffe | Agents for Humans 2026")
