import os
from dotenv import load_dotenv

from google.adk import Agent

load_dotenv()

root_agent = Agent(
    name="transcript_summarization_agent",
    description="Summarizes chat transcripts.",
    model=os.getenv("MODEL", "gemini-2.0-flash-exp"),
    instruction="Summarize the provided chat transcript.",
)