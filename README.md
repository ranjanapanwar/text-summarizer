# AI Text Summarizer

A web app that summarizes text using Google's T5-small model, built with Gradio and deployed on Hugging Face Spaces.

## How it works

Paste any article or block of text into the input box and the app returns a concise summary. It uses the T5-small transformer model with beam search decoding for quality output.

## Stack

- **Model:** `t5-small` (via Hugging Face Transformers)
- **UI:** Gradio
- **Deployment:** Hugging Face Spaces

## Dependencies

- `gradio==4.44.0`
- `transformers==4.44.2`
- `torch==2.4.1`
- `accelerate==1.0.1`

## Running locally

```bash
pip install -r requirements.txt
python app.py
```

## Deployment

Pushes to `main` are automatically synced to Hugging Face Spaces via GitHub Actions.
