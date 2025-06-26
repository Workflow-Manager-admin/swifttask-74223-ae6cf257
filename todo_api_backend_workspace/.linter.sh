#!/bin/bash
cd /home/kavia/workspace/code-generation/swifttask-74223-ae6cf257/todo_api_backend_workspace/todo_api_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

