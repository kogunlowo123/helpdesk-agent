"""Test configuration for Helpdesk Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "helpdesk-agent", "category": "IT Operations"}
