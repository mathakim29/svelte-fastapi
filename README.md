# Svelte FastAPI Template

Small Svelte + FastAPI starter with Tailwind CSS and clean history routing.

The template uses the browser History API for routing, so URLs stay clean
without a hash or router dependency.

## Setup

```bash
uv sync
bun install
```

## Run

Start the API with `uv run api`, then run the frontend in another terminal with `bun run dev`.

The sample page includes a `/api/health` request and `/` and `/about` routes. Add Vite proxy settings in `vite.config.js` when serving the frontend and API on separate ports.
