# AI Platform Journey
My path from DevOps architect to AI platform architect. One folder per phase.

## Setup (Phase 1, Topic 1)
- MacBook (Apple Silicon, 8 GB RAM), macOS <version>
- Python 3.12 with uv; VS Code + Jupyter
- Ollama running llama3.2:3b locally (≈2 GB)
- Gemini API (free tier) as the hosted model; key kept in .env (not committed)

## Constraint
8 GB RAM, so local models are limited to ~3B; larger models run in Google Colab.

## Run
uv run python phase-1/hello-llm.py