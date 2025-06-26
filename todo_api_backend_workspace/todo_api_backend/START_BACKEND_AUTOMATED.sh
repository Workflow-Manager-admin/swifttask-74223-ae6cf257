#!/bin/bash
# Script to automatically start the Flask backend server in development mode with all dependencies ensured.
set -e
cd "$(dirname "$0")"
if [ ! -d venv ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
export FLASK_ENV=development
export FLASK_APP=run.py
exec flask run --port=5001
