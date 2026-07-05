"""Helpdesk Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class SupportTicket(BaseModel):
    """SupportTicket for Helpdesk Agent."""
    id: str
    title: str
    category: str
    priority: str
    status: str
    user_id: str
    assigned_to: str | None


class DiagnosticResult(BaseModel):
    """DiagnosticResult for Helpdesk Agent."""
    checks_run: list[str]
    findings: list[dict]
    suggested_action: str
    confidence: float

