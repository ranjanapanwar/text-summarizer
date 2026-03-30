---
title: AI Text Summarizer
emoji: 📝
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "6.9.0"
python_version: "3.11"
app_file: app.py
pinned: false
---

# AI Text Summarizer

A simple AI-powered text summarizer built with Gradio and Groq API. Built as a warm-up project to learn API integration and Gradio UI basics.

## Features

- Paste any text and get a concise bullet-point summary
- Powered by Groq API (LLaMA 3.1 8B)
- Error handling for invalid API key and rate limits
- Clean Gradio UI

## Stack

- `gradio` — UI
- `groq` — LLM API (LLaMA 3.1 8B)
- `python-dotenv` — API key management
- `uv` — dependency management

## Running Locally

```bash
uv run app.py
```

Open `http://localhost:7860`

## Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key |

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_key_here
```