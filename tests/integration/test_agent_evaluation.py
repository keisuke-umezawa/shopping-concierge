"""Integration tests for the Shopping Concierge Agent using ADK evaluation."""

import os

import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator

FIXTURE_DIR = os.path.join(os.path.dirname(__file__), "fixture")

SKIP_REASON = (
    "Skipping ADK evaluation test: requires Google Cloud credentials. "
    "Set GOOGLE_APPLICATION_CREDENTIALS or run 'gcloud auth application-default login'."
)


def _has_gcp_credentials() -> bool:
    """Check if Google Cloud credentials are available."""
    if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        return True
    default_creds_path = os.path.expanduser(
        "~/.config/gcloud/application_default_credentials.json"
    )
    return os.path.exists(default_creds_path)


@pytest.mark.asyncio
@pytest.mark.skipif(not _has_gcp_credentials(), reason=SKIP_REASON)
async def test_shopping_concierge_basic_evaluation():
    """Test the shopping concierge agent's basic ability via a session file.

    This test uses the ADK AgentEvaluator to evaluate the agent against
    predefined test cases in the test.json file.

    Note: This test requires Google Cloud credentials to be configured.
    It will be skipped in CI environments without credentials.
    """
    await AgentEvaluator.evaluate(
        agent_module="shopping_concierge",
        eval_dataset_file_path_or_dir=os.path.join(
            FIXTURE_DIR, "shopping_concierge_basic.test.json"
        ),
        num_runs=1,
    )
