# Helpdesk Agent Architecture

IT helpdesk agent that handles user support requests, troubleshoots common IT issues, automates password resets, manages software installations, and escalates complex issues with full context to Tier 2 support.

## Domain Tools

- **search_knowledge_base**: Search IT knowledge base for solutions to common issues
- **diagnose_issue**: Run diagnostic checks for a reported IT issue
- **execute_remediation**: Execute an automated remediation action
- **create_ticket**: Create an IT support ticket with categorization and priority
- **escalate_ticket**: Escalate a ticket to Tier 2 with diagnostic context