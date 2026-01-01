from google.adk.agents import Agent

# -----------------------------
# TEACHER AGENT
# -----------------------------
teacher_agent = Agent(
    name="teacher_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are a Teacher.\n"
        "Explain concepts clearly, step by step, with proper definitions and examples.\n"
        "Your tone should be professional and educational."
    )
)

# -----------------------------
# STUDENT AGENT
# -----------------------------
student_agent = Agent(
    name="student_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are a Student.\n"
        "Explain concepts in very simple words, as a beginner would.\n"
        "Keep the explanation short and easy to understand."
    )
)

# Root agent (entry point)
root_agent = teacher_agent


