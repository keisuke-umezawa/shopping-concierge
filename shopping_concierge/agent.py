"""Main agent definition for the Shopping Concierge Agent."""

import os

from google.adk.agents import LlmAgent

from shopping_concierge.prompt import AGENT_INSTRUCTIONS

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION", "us-central1")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.0-flash-exp")

agent = LlmAgent(
    model=f"vertex_ai/{MODEL_NAME}",
    instruction=AGENT_INSTRUCTIONS,
    name="shopping_concierge",
    description="A shopping concierge agent that helps users find and "
    "recommend products",
)
