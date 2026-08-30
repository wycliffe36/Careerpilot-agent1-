import streamlit as st
from langchain_groq import ChatGroq

st.set_page_config(page_title="CareerPilot AI", page_icon="🚀", layout="wide")

GROQ_KEY = st.secrets["GROQ_API_KEY"]

st.title("🚀 CareerPilot Agent")
st.caption("Agents for Humans 2026 | Live in Nairobi")

llm = ChatGroq(model="openai/gpt-oss-20b", api_key=GROQ_KEY, temperature=0.3)

role = st.selectbox("Target Role", ["AI Engineer", "Data Scientist", "Full Stack Developer", "Cloud Engineer", "Data Analyst"])
level = st.selectbox("Level", ["Student", "Entry", "Mid", "Senior"])

job = st.text_area("📋 Paste Job Advert", height=200, placeholder="Paste the full job description here...")
skills = st.text_area("🧑‍💻 Your Skills / CV", height=150, value="Skills: Python (2 years), SQL, Streamlit, Git, Pandas\nProjects: CareerPilot Agent (Groq + LangChain), Student Management System\nLearning: LangChain, RAG, AWS\nSoft skills: Teamwork, Communication\nBased in Nairobi")

if st.button("🚀 Generate Roadmap", type="primary", use_container_width=True):
    if not job.strip():
        st.warning("Please paste a job advert first")
        st.stop()
    with st.spinner("Agents analyzing..."):
        prompt = f"""
You are CareerPilot AI, an expert career coach in Kenya.
Target Role: {role}
Level: {level}
Job Advert: {job}
Candidate Profile: {skills}

Give:
1. Match Score % with reason
2. Top Skill Gaps
3. 30-60-90 Day Roadmap for Nairobi learner
4. 3 Resume bullet points to add
5. 5 Interview Questions + short answers
Make it concise, actionable, and encouraging.
"""
        response = llm.invoke(prompt)
        st.success("✅ Roadmap Generated!")
        st.markdown(response.content)
        st.balloons()

st.divider()
st.caption("Built by Wycliffe | Agents for Humans 2026")
