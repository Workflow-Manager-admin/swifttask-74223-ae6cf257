# How to Run the Vue Frontend (todo_frontend_app)

These steps will install dependencies and launch the Vue development server, with calls routed to your Flask backend at `http://localhost:5000`.

## 1. Install Dependencies

Open a terminal and run:
```sh
cd todo_frontend_app_workspace/todo_frontend_app
npm install
```

## 2. Set the API Base URL

The code fetches the API base URL from `import.meta.env.VITE_TODO_API_BASE`. To ensure requests go to the Flask backend (by default on `http://localhost:5000`):

In the project root (where `package.json` is), create or update a file named `.env.local`:
```env
VITE_TODO_API_BASE=http://localhost:5000
```
> - `.env.local` is loaded by Vite automatically, and takes effect for local development.

## 3. Start the Development Server

Run:
```sh
npm run dev
```
The app will be available at http://localhost:3000

## 4. Platform-Specific Tips

- **Windows/macOS/Linux:** These instructions work on all platforms. Use a terminal like PowerShell, Terminal.app, or bash.
- If `npm` is not found, install [Node.js (includes npm)](https://nodejs.org/).

## 5. Proxy/Networking (Advanced)

If CORS errors occur or you want `/api` to automatically forward to Flask, add a proxy to `vite.config.ts` (not required if backend sends CORS headers):

```js
// Inside 'server:' in vite.config.ts
proxy: {
  '/api': 'http://localhost:5000',
}
```
Then update your frontend requests like: `/api/tasks`.

## 6. Stopping the Server

- To stop: Press `Ctrl+C` in the terminal where `npm run dev` is running.

***

## Quick Reference

```sh
# 1. Navigate to frontend folder
cd todo_frontend_app_workspace/todo_frontend_app

# 2. Install dependencies
npm install

# 3. Set API base (.env.local)
echo "VITE_TODO_API_BASE=http://localhost:5000" > .env.local

# 4. Start dev server
npm run dev
```
