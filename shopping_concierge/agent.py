"""Main agent definition for the Shopping Concierge Agent."""

import os

from google.adk.agents import LlmAgent

from shopping_concierge.prompt import AGENT_INSTRUCTIONS

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION", "us-central1")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.0-flash-exp")
MODEL_BACKEND = os.getenv("MODEL_BACKEND", "vertex_ai")


def _get_model():
    """Get the model based on the MODEL_BACKEND environment variable.

    Returns:
        Either a string for Vertex AI models or a LiteLlm instance for
        local/LiteLLM-supported models.
    """
    backend = MODEL_BACKEND.lower()
    if backend == "litellm":
        from google.adk.models.lite_llm import LiteLlm

        return LiteLlm(model=MODEL_NAME)
    return f"vertex_ai/{MODEL_NAME}"


agent = LlmAgent(
    model=_get_model(),
    instruction=AGENT_INSTRUCTIONS,
    name="shopping_concierge",
    description=(
        "A shopping concierge agent that helps users find and "
        "recommend products"
    ),
)
