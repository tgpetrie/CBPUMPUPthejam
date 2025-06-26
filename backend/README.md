# Backend Setup & Usage

This guide explains how to run the Flask backend server.

## 1. First-Time Setup

Before running the server for the first time, you need to make the helper scripts executable. You only need to do this once.

Open your terminal, navigate to the `backend` directory, and run this command:

```bash
chmod +x *.sh
```

This command gives permission to run all files ending in `.sh` (like `start.sh` and `clear-cache.sh`).

## 2. Running the Server

To start the backend server, navigate to the `backend` directory in your terminal and run the following command:

```bash
./start.sh
```

**Why `./`?** The `./` tells your terminal to look for the `start.sh` script in the current directory.

The server will automatically find an open port and configure the frontend to connect to it.

## 3. Clearing the Cache

If you ever encounter strange issues, you can clear the Python cache files by running:

```bash
./clear-cache.sh
```

## 4. Troubleshooting

### Problem: "permission denied" when running a script

If you see `zsh: permission denied: ./start.sh`, it means you haven't made the scripts executable yet. Run the one-time setup command:

```bash
chmod +x *.sh
```

### Problem: Frontend shows old data or "404 Not Found" errors

If the web page is making calls to old API routes (like `/api/component/...`), your frontend development server is likely serving a cached version of your app.

**Solution:** Stop your frontend server (usually with `CTRL+C` in its terminal) and restart it.
