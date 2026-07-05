"""Helpdesk Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_search_knowledge_base():
    """Test Search IT knowledge base for solutions to common issues."""
    tools = AgentTools()
    result = await tools.search_knowledge_base(query="test", category="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_diagnose_issue():
    """Test Run diagnostic checks for a reported IT issue."""
    tools = AgentTools()
    result = await tools.diagnose_issue(issue_type="test", user_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_execute_remediation():
    """Test Execute an automated remediation action."""
    tools = AgentTools()
    result = await tools.execute_remediation(action="test", target_user="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_create_ticket():
    """Test Create an IT support ticket with categorization and priority."""
    tools = AgentTools()
    result = await tools.create_ticket(title="test", description="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.helpdesk_agent_agent import HelpdeskAgentAgent
    agent = HelpdeskAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
