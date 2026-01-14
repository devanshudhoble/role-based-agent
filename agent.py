from google.adk.agents import LlmAgent, ParallelAgent

MODEL = "groq/llama-3.1-8b-instant"

# -------------------------
# Teacher Agent
# -------------------------
teacher_agent = LlmAgent(
    name="TeacherAgent",
    model=MODEL,
    instruction=(
        "You are a TEACHER.\n"
        "Explain answers clearly, formally, and in a structured teaching style.\n"
        "When asked about yourself, state clearly that you are a teacher."
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
        "Answer from a learner’s perspective using simple language.\n"
        "When asked about yourself, state clearly that you are a student."
    ),
    output_key="student_response"
)

# -------------------------
# PARALLEL MULTI-AGENT (CORRECT)
# -------------------------
role_comparison_agent = ParallelAgent(
    name="RoleComparisonAgent",
    sub_agents=[teacher_agent, student_agent],
    description="Runs teacher and student agents in parallel on the same question"
)

# Root agent
root_agent = role_comparison_agent
