
import os
import streamlit as st
from langchain_groq import ChatGroq

# Get key
try:
    GROQ_KEY = st.secrets["GROQ_API_KEY"]
except:
    GROQ_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_KEY, temperature=0.3)

def careerpilot_agent(job_desc, user_skills, target_role, exp_level):
    prompt = f"""
    You are CareerPilot Agent for Kenya job seekers.
    Target: {target_role} | Level: {exp_level}
    Job: {job_desc}
    User: {user_skills}

    Provide:
    1. Match Score %
    2. Skill Gap (Have vs Missing)
    3. 30-60-90 Day Roadmap
    4. Tailored CV Bullets (3)
    5. Cover Letter Paragraph
    6. Interview Questions

    Be concise, actionable.
    """
    return llm.invoke(prompt).content
