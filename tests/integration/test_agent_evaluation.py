"""Integration tests for the Shopping Concierge Agent using ADK evaluation."""

import os

import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator

FIXTURE_DIR = os.path.join(os.path.dirname(__file__), "fixture")


@pytest.mark.asyncio
async def test_shopping_concierge_basic_evaluation():
    """Test the shopping concierge agent's basic ability via a session file.

    This test uses the ADK AgentEvaluator to evaluate the agent against
    predefined test cases in the test.json file.
    """
    await AgentEvaluator.evaluate(
        agent_module="shopping_concierge",
        eval_dataset_file_path_or_dir=os.path.join(
            FIXTURE_DIR, "shopping_concierge_basic.test.json"
        ),
        num_runs=1,
    )
