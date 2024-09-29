# open-copilot-cli

[![Continuous Integration](https://github.com/youzarsiph/open-copilot-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/open-copilot-cli/actions/workflows/ci.yml)
[![Continuous Deployment](https://github.com/youzarsiph/open-copilot-cli/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/open-copilot-cli/actions/workflows/cd.yml)
[![Black](https://github.com/youzarsiph/open-copilot-cli/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/open-copilot-cli/actions/workflows/black.yml)
[![Ruff](https://github.com/youzarsiph/open-copilot-cli/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/open-copilot-cli/actions/workflows/ruff.yml)

Open Copilot, your AI assistant in your terminal.

## Getting Started

To begin, install the package:

```bash
pip install open-copilot-cli
```

Export your `HF_TOKEN` as an environment variable, you can get your token from [HuggingFace](https://huggingface.co/settings/tokens):

Bash:

```bash
export HF_TOKEN=hf_**********************************
```

Powershell:

```powershell
$env:HF_TOKEN = "hf_**********************************"
```

You are now ready to utilize the application.

## Usage

To view the help options, run:

```bash
open-copilot --help
```

### Ask questions

You can ask questions using natural language:

```bash
open-copilot ai 'list all files in the current directory'
```

### Chat

Engage in a chat with OpenCopilot:

```bash
open-copilot chat --

# Export chat history
open-copilot chat -e chat-history.json

# Import chat history
open-copilot chat -h chat-history.json

# Import chat history and then export it after the session
open-copilot chat -h chat-history.json -e chat-history.json
```

### Custom Large Language Models (LLMs)

Utilize custom LLMs:

```bash
open-copilot chat -m 'mistralai/Mistral-Nemo-Instruct-2407'
```

## License

This project is licensed under the MIT License.
