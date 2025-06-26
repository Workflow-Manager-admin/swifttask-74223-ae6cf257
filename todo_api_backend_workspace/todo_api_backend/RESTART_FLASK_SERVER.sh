#!/bin/bash
# Restarts the Flask backend development server on port 5001 using the virtualenv

set -e

cd "$(dirname "$0")"

# Stop any process using port 5001 (forcibly, if running)
PID=$(lsof -ti:5001 || true)
if [ -n "$PID" ]; then
    echo "Stopping Flask development server running on port 5001 (PID: $PID)..."
    kill -9 $PID
    sleep 1
fi

# Activate virtualenv
if [ ! -d venv ]; then
    python3 -m venv venv
fi
source venv/bin/activate

# Ensure dependencies are installed
pip install --upgrade pip
pip install -r requirements.txt

# Set Flask variables
export FLASK_ENV=development
export FLASK_APP=run.py

# Start Flask server on port 5001
echo "Starting Flask development server on port 5001..."
flask run --port=5001
