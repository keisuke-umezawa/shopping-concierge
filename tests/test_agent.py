"""Tests for the Shopping Concierge Agent."""

import pytest

from shopping_concierge.agent import agent


def test_agent_exists():
    """Test that the agent is properly initialized."""
    assert agent is not None
    assert agent.name == "shopping_concierge"


def test_agent_has_instruction():
    """Test that the agent has instruction."""
    assert agent.instruction is not None
    assert len(agent.instruction) > 0


@pytest.mark.asyncio
async def test_agent_basic_interaction():
    """Test basic agent interaction."""
    pass
