# Restarting the Vue Frontend Server to Apply Environment Variable Changes

To ensure your Vue frontend uses the updated API backend (now set to `http://localhost:5001` in `.env.local`), follow these steps to **stop** and **restart** the development server:

---

## 1. Stop the Running Vue Dev Server

If the Vue app is currently running (you see the development logs and file change reloads in your terminal), you need to stop it:

- **In the terminal where the Vue dev server is running, press:**  
  **`Ctrl + C`**

This will gracefully shut down the running server process.

---

## 2. Ensure `.env.local` is Correct

Make sure your `.env.local` file in the project root (`todo_frontend_app_workspace/todo_frontend_app`) contains:
```
VITE_TODO_API_BASE=http://localhost:5001
```

---

## 3. Restart the Dev Server

In your terminal, navigate to the frontend folder (if you’re not there already):
```sh
cd todo_frontend_app_workspace/todo_frontend_app
```

Then **start the server again**:
```sh
npm run dev
```

- The frontend will now run at [http://localhost:3000](http://localhost:3000) and proxy API requests to the backend at `http://localhost:5001`.

---

## Troubleshooting

- If you get an error that the port is already in use, ensure no previous dev server instances are running.
- If environment variable changes don’t seem to take effect, confirm you updated `.env.local` in the correct folder (same level as `package.json`), then stop and restart the server as above.

---

**Tip:** You will need to repeat these steps anytime you make changes to `.env.local` or other environment/configuration files.

Task completed: Added explicit step-by-step instructions for stopping and restarting the Vue frontend server to use updated backend configuration.
