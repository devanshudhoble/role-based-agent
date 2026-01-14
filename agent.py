from google.adk.agents import LlmAgent, SequentialAgent

MODEL = "groq/llama-3.1-8b-instant"

# -------------------------
# Teacher Agent
# -------------------------
teacher_agent = LlmAgent(
    name="TeacherAgent",
    model=MODEL,
    instruction=(
        "You are a TEACHER.\n"
        "When asked any question, respond like an experienced teacher.\n"
        "Explain concepts clearly, formally, and in a structured way.\n"
        "When asked about yourself, clearly state that you are a teacher."
    ),
    output_key="teacher_response"
)

# -------------------------
# Student Agent
# -------------------------
student_agent = LlmAgent(
    name="StudentAgent",
    model=MODEL,
    instruction=(
        "You are a STUDENT.\n"
        "When asked any question, respond like a learner.\n"
        "Explain things in simple words and from a beginner’s perspective.\n"
        "When asked about yourself, clearly state that you are a student."
    ),
    output_key="student_response"
)

# -------------------------
# Multi-Agent Controller
# -------------------------
role_comparison_agent = SequentialAgent(
    name="RoleComparisonAgent",
    sub_agents=[teacher_agent, student_agent],
    description="Runs teacher and student agents on the same question"
)

# Root agent (IMPORTANT)
root_agent = role_comparison_agent
