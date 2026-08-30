from strands import Agent, tool
from strands.models.bedrock import BedrockModel

@tool
def analyze_job_tool(job_text: str) -> dict:
    """Analyzes job advert and extracts skills, keywords, ATS requirements"""
    return {
        "skills": ["Communication", "Marketing", "SEO"],
        "keywords": ["Campaign", "Digital Marketing", "SEO"],
        "summary": job_text[:300],
        "level": "Mid-Level"
    }

@tool
def tailor_cv_tool(cv_text: str, job_summary: str) -> str:
    """Tailors user CV to match job summary and keywords"""
    return f"""
--- TAILORED CV ---

Target Role Summary: {job_summary}

Professional Summary:
Results-driven professional with experience aligned to {job_summary}.

Key Skills Matched: SEO, Campaign Management, Communication

Original CV Base:
{cv_text}

Optimized for ATS with keywords.
"""

@tool
def generate_cover_tool(job_summary: str, user_name: str = "Applicant") -> str:
    """Generates personalized cover letter for the job"""
    return f"""
Dear Hiring Manager,

I am excited to apply for the role summarized as: {job_summary}

My experience aligns with your requirements in SEO and Campaign Management.

I would love to contribute to your team.

Sincerely,
{user_name}
"""

@tool
def generate_qa_tool(job_summary: str) -> list:
    """Generates 5 interview Q&A for the job"""
    return [
        f"Q: Why do you want this role? A: Because {job_summary}",
        "Q: Tell us about your experience in Campaigns?",
        "Q: How do you handle SEO challenges?",
        "Q: What is your strength?",
        "Q: Where do you see yourself in 2 years?"
    ]

model = BedrockModel(
    model_id="us.anthropic.claude-3-haiku-20240307-v1:0",
    region_name="us-east-1",
    temperature=0.3
)

career_agent = Agent(
    model=model,
    tools=[analyze_job_tool, tailor_cv_tool, generate_cover_tool, generate_qa_tool],
    system_prompt="You are CareerPilot Agent. You are an autonomous Professional Agent that helps job seekers. You understand job adverts, you take action to tailor CVs, write cover letters, and prepare interview answers. You help humans get hired."
)
