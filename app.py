import streamlit as st
from agent import career_agent

st.set_page_config(page_title="CareerPilot Agent", layout="centered")
st.title("CareerPilot Agent")
st.subheader("Autonomous AI Agent for Job Seekers - Agents for Humans Hackathon")
st.markdown("**Track:** Professional Agents | **Built with:** Strands Agents SDK")

job_text = st.text_area("Paste Job Advert Here (from BrighterMonday / LinkedIn)", height=200)
cv_text = st.text_area("Paste Your CV Here", height=200)
name = st.text_input("Your Name", "John Doe")

if st.button("Run CareerPilot Agent"):
    if not job_text or not cv_text:
        st.warning("Paste both Job and CV")
    else:
        with st.spinner("Agent is analyzing, tailoring CV, writing cover letter..."):
            prompt = f"Job advert: {job_text}. User CV: {cv_text}. User Name: {name}. Analyze job, tailor CV, generate cover letter and interview Q&A."
            result = career_agent(prompt)
            st.success("Application Pack Ready!")
            st.markdown("### Agent Result")
            st.write(result)
