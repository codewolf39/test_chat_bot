# Local AI Chatbot with Ollama

A locally running conversational AI chatbot built with Python, Gradio, Ollama, and Llama 3.2.

## Features

- Local LLM inference using Ollama
- Interactive chat interface built with Gradio
- Multi-turn conversations with conversation history
- System prompts for controlling assistant behaviour
- Streaming responses (if enabled in the current implementation)
- Experiments with prompt injection and confidential-data disclosure using synthetic test data

## Tech Stack

- Python
- Ollama
- Llama 3.2
- Gradio
- uv for Python dependency management

## Prerequisites

- Python
- [Ollama](https://ollama.com/)
- [uv](https://docs.astral.sh/uv/)
- Git

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd gradio_chat_bot
```

### 2. Download the model

```bash
ollama pull llama3.2
```

### 3. Install dependencies

If the repository includes `pyproject.toml` and `uv.lock`:

```bash
uv sync
```

### 4. Run the application

```bash
uv run app.py
```

Open the local URL printed in the terminal, usually:

`http://127.0.0.1:7860`

## How It Works

Gradio receives user messages and provides conversation history to a Python callback. The application prepares the message list, sends it to Ollama, and returns the model's response to the chat interface.

## Security Testing

The project includes experiments for evaluating prompt-injection resistance and sensitive-information disclosure using fictional test data.

These experiments are educational and do not constitute a comprehensive security audit.

## Limitations

- Model responses may be inaccurate.
- Conversation history is provided as context; it is not permanent memory.
- Prompt instructions alone cannot guarantee confidentiality.
- The Ollama model must be installed locally.

## License

MIT
