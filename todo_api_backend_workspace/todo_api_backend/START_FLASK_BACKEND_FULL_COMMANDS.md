# How to Start the Flask Backend Server (todo_api_backend) — Full Command Reference

Follow these exact steps in your terminal **from the project root** (`/home/kavia/workspace/code-generation/swifttask-74223-ae6cf257`).  
This will set up and run your Flask backend API for local development.

---

## 1. Change to the backend directory
```bash
cd todo_api_backend_workspace/todo_api_backend
```

---

## 2. (One-time) Create and activate a Python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
# (On Windows: venv\Scripts\activate)
```

---

## 3. Install all backend dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. (Optional but recommended) Set Flask development mode for auto-reload
```bash
export FLASK_ENV=development
# (On Windows: set FLASK_ENV=development)
```

---

## 5. (Required for flask CLI) Set the FLASK_APP variable
```bash
export FLASK_APP=run.py
# (On Windows: set FLASK_APP=run.py)
```

---

## 6. Start the backend server

### Method 1: (Recommended) Use Flask CLI for hot-reload
```bash
flask run
```

### OR

### Method 2: Run via Python
```bash
python run.py
```

Your API will be live at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  
Swagger (API docs): [http://localhost:5000/docs/](http://localhost:5000/docs/)

---

## 7. Stopping the Server
Use `Ctrl+C` in your terminal.

---

## Notes

- Always start each terminal session by activating your virtual environment:
  ```
  source venv/bin/activate
  ```
- For troubleshooting or more details, see `README.md`.

---
