# To-Do API Backend – Local Development Guide

This guide explains how to set up and run the Flask backend server for the To-Do List application on your local machine.

---

## Prerequisites

- **Python 3.8+** installed (recommend using [pyenv](https://github.com/pyenv/pyenv) or [virtualenv](https://virtualenv.pypa.io/))

---

## 1. Clone the Repository & Enter the Backend Directory

If you haven't already:

```bash
git clone <repo-url>
cd <repo-directory>/todo_api_backend_workspace/todo_api_backend
```

---

## 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # (on Windows: venv\Scripts\activate)
```

---

## 3. Install Python Dependencies

Install all required dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. Set Environment Variables (Optional)

This project does not require any mandatory environment variables by default. You can run the server as is.
If you want to run Flask in development mode (auto-reload & better error messages):

```bash
export FLASK_ENV=development
```

---

## 5. Run the Flask Development Server

Start the backend server using:

```bash
python run.py
```
or for hot-reload:
```bash
flask run
```
**Note:** By default, the server will be available at `http://127.0.0.1:5000/`.

---

## 6. API Documentation

Once running, interactive API docs (Swagger UI) will be available at:

- [http://localhost:5000/docs/](http://localhost:5000/docs/)

---

## 7. Stopping the Server

Press `Ctrl+C` in your terminal to stop the Flask development server.

---

## 8. Troubleshooting

- Make sure you are in the correct directory (`todo_api_backend_workspace/todo_api_backend`) when running commands.
- If you need to reinstall packages:  
  ```bash
  pip install --force-reinstall -r requirements.txt
  ```
- For permission issues, try:  
  ```bash
  pip install --user -r requirements.txt
  ```

---

**You're all set to connect the frontend app to this backend API!**
