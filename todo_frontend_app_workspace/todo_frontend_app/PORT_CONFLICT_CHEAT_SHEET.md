# Fixing Port Conflicts for Vue/Vite Dev Server

If you cannot open the Vue frontend or get an error like "port 3000/5173 is already in use", follow these steps:

---

## 1. Kill Any Process On Port 3000 or 5173

In your terminal, **from the `todo_frontend_app_workspace/todo_frontend_app` folder:**
```sh
bash KILL_FRONTEND_PORTS.sh
```
This script will forcibly kill any process using ports 3000 or 5173 (the default and alternate dev ports for Vite/Vue).

---

## 2. (Alternative) Kill Individual Ports Manually

If you do not want to use the script, you can run:
```sh
lsof -i :3000
lsof -i :5173
```
If any processes are listed, kill them with:
```sh
kill -9 <PID>
```
(Replace `<PID>` with the actual process ID shown.)

---

## 3. Restart the Frontend

Then start the frontend dev server again:
```sh
npm run dev
```

The app should now be accessible at [http://localhost:3000](http://localhost:3000) (or `0.0.0.0:3000`/your local IP).

---

## Troubleshooting

- If you still get address-in-use errors, make sure all terminals running `npm run dev` or `vite` are closed, or log out/reboot as a last resort.
- Some systems or CI environments may restrict the `lsof` or `kill` commands; check permissions.
- For WSL or Windows: run the script or equivalent PowerShell commands as administrator.

---

**Reference:**
- See also: `DEV_RESTART_FRONTEND.md`, `DEV_STARTUP.md` in the project root for more setup tips.
