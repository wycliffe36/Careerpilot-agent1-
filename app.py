import streamlit as st
import os
from langchain_groq import ChatGroq

st.set_page_config(page_title="CareerPilot AI", page_icon="🚀", layout="wide")

GROQ_KEY = st.secrets.get("GROQ_API_KEY") if "GROQ_API_KEY" in st.secrets else None

if not GROQ_KEY:
    st.error("Add GROQ_API_KEY in Streamlit Secrets")
    st.stop()

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_KEY, temperature=0.3)

st.title("🚀 CareerPilot Agent")
role = st.selectbox("Target Role", ["AI Engineer","Data Scientist","Full Stack","Cloud","Data Analyst"])
level = st.selectbox("Level", ["Student","Entry","Mid","Senior"])
job = st.text_area("Paste Job Advert", height=200)
skills = st.text_area("Your Skills", height=200)

if st.button("Generate", type="primary"):
    if not job:
        st.warning("Paste job first")
    else:
        with st.spinner("Analyzing..."):
            prompt = f"Role:{role} Level:{level} Job:{job} Skills:{skills} Provide Match Score, Skill Gap, 30-60-90 Roadmap, CV bullets, Interview Qs"
            ans = llm.invoke(prompt).content
            st.markdown(ans)
