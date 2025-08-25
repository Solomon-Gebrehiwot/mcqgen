## LangChain Text Generator CLI

A minimal CLI for generating text with LangChain using OpenAI or Ollama providers.

### Installation

1) Install dependencies:

```bash
python3 -m pip install -r /workspace/requirements.txt
```

2) Configure providers (as needed):

- OpenAI: set `OPENAI_API_KEY` in your environment.
- Ollama: ensure `ollama` is installed and running; set `OLLAMA_HOST` if not default.

### Usage

Basic dry-run (no network call):

```bash
python3 /workspace/textgen.py --provider openai --model gpt-4o-mini -p "Write a haiku" --dry-run
```

OpenAI generation:

```bash
export OPENAI_API_KEY=your_key_here
python3 /workspace/textgen.py --provider openai --model gpt-4o-mini -p "List three creative icebreaker questions" -t 0.6
```

Ollama generation:

```bash
python3 /workspace/textgen.py --provider ollama --model llama3.1:8b -p "Explain quantum entanglement simply" -t 0.7
```

Optional flags:

- `--max-tokens/-m`: limit completion length if supported by the provider
- `--temperature/-t`: sampling temperature
- `--dry-run`: print configuration without invoking the model

