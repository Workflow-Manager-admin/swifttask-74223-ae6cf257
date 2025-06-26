# How to Start the Flask Backend Server (todo_api_backend)

Follow these copy-pasteable commands to set up and launch the backend API.

---

## Step 1: Enter the Backend Directory

```bash
cd todo_api_backend_workspace/todo_api_backend
```

---

## Step 2: (Recommended) Set Up & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # (on Windows: venv\Scripts\activate)
```

---

## Step 3: Install All Python Requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Step 4: (Optional) Set Development Mode for Flask (hot reload, better errors)

```bash
export FLASK_ENV=development
```
*(On Windows: `set FLASK_ENV=development`)*

---

## Step 5: Start the Flask Backend Server

### Method 1: (preferred if you want auto-reloading)
```bash
flask run
```

### Method 2: (classic Python execution)
```bash
python run.py
```

By default, the server will run at:  
**http://127.0.0.1:5001/**

---

## Step 6: Access the Interactive API Docs

Available at:  
**http://localhost:5001/docs/**

---

## Step 7: Stopping the Server

To stop, use `Ctrl+C` in your terminal.

---

Common troubleshooting and more details are in the README.md.
