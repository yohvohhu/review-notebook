# Smart Mistake Notebook

Prototype of a spaced-repetition notebook with FastAPI backend and Vue 3 PWA frontend.

## Backend

- FastAPI + SQLModel (SQLite by default)
- JWT auth (access/refresh)
- Basic card CRUD

### Install dependencies

If your environment blocks direct internet access via an intercepting proxy, use the helper script to install backend requirements without proxy variables:

```
./scripts/install_deps.sh
```

### Environment variables
- `DATABASE_URL` (default `sqlite:///./app.db`)
- `JWT_SECRET` (set in production)

### Run locally
```
uvicorn app.main:app --reload
```

## Frontend

Vue 3 + Vite + TypeScript with Pinia and Element Plus. PWA is enabled via `vite-plugin-pwa`.

### Run locally
```
npm install
npm run dev
```

## Docker

```
docker compose up -d --build
```
Backend exposed at `http://localhost` through Caddy reverse proxy. API is served under `/api`.

## Seed Data

A simple seed script inserts one user and three sample cards:
```
python backend/seed.py
```
