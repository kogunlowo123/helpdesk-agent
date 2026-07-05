#!/bin/bash
set -euo pipefail
echo "Setting up Helpdesk Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
