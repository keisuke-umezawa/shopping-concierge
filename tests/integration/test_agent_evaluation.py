"""Integration tests for the Shopping Concierge Agent using ADK evaluation."""

import os

import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator

FIXTURE_DIR = os.path.join(os.path.dirname(__file__), "fixture")

SKIP_REASON = (
    "Skipping ADK evaluation test: requires credentials. "
    "Set GOOGLE_API_KEY for Gemini API, or GOOGLE_APPLICATION_CREDENTIALS / "
    "'gcloud auth application-default login' for Vertex AI."
)


def _has_model_credentials() -> bool:
    """Check if credentials for running the model are available."""
    if os.environ.get("GOOGLE_API_KEY"):
        return True
    if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        return True
    default_creds_path = os.path.expanduser(
        "~/.config/gcloud/application_default_credentials.json"
    )
    return os.path.exists(default_creds_path)


@pytest.mark.asyncio
@pytest.mark.skipif(not _has_model_credentials(), reason=SKIP_REASON)
async def test_shopping_concierge_basic_evaluation():
    """Test the shopping concierge agent's basic ability via a session file.

    This test uses the ADK AgentEvaluator to evaluate the agent against
    predefined test cases in the test.json file.

    Note: This test requires credentials to be configured (either GOOGLE_API_KEY
    for Gemini API or GCP credentials for Vertex AI).
    """
    await AgentEvaluator.evaluate(
        agent_module="shopping_concierge",
        eval_dataset_file_path_or_dir=os.path.join(
            FIXTURE_DIR, "shopping_concierge_basic.test.json"
        ),
        num_runs=1,
    )
