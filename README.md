# Helpdesk Agent

[![CI](https://github.com/kogunlowo123/helpdesk-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/helpdesk-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: IT Operations | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

IT helpdesk agent that handles user support requests, troubleshoots common IT issues, automates password resets, manages software installations, and escalates complex issues with full context to Tier 2 support.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `search_knowledge_base` | Search IT knowledge base for solutions to common issues |
| `diagnose_issue` | Run diagnostic checks for a reported IT issue |
| `execute_remediation` | Execute an automated remediation action |
| `create_ticket` | Create an IT support ticket with categorization and priority |
| `escalate_ticket` | Escalate a ticket to Tier 2 with diagnostic context |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/helpdesk/search` | Search knowledge base |
| `POST` | `/api/v1/helpdesk/diagnose` | Diagnose issue |
| `POST` | `/api/v1/helpdesk/remediate` | Execute remediation |
| `POST` | `/api/v1/helpdesk/tickets` | Create ticket |
| `POST` | `/api/v1/helpdesk/tickets/{ticket_id}/escalate` | Escalate ticket |

## Features

- Issue Triage
- Troubleshooting
- Self Service
- Escalation
- Knowledge Search

## Integrations

- Servicenow
- Jira Service Management
- Zendesk
- Active Directory
- Sccm

## Architecture

```
helpdesk-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── helpdesk_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**ITSM Platform + Knowledge Base + Active Directory**

---

Built as part of the Enterprise AI Agent Platform.
