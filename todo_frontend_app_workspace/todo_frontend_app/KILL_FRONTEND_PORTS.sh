#!/bin/bash
# Kills any processes bound to ports 3000 or 5173 (both common for Vite/Vue dev)
# Usage: bash KILL_FRONTEND_PORTS.sh

PORTS=(3000 5173)

for PORT in "${PORTS[@]}"
do
  # Find process IDs using the port and kill them
  PIDS=$(lsof -i :$PORT -t 2>/dev/null)
  if [ -n "$PIDS" ]; then
    echo "Killing processes using port $PORT: $PIDS"
    kill -9 $PIDS
  else
    echo "No process found using port $PORT"
  fi
done

echo "Port cleanup complete. You can now start the frontend dev server without port conflicts."
