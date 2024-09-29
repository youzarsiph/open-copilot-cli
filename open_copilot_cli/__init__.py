"""
OpenCopilot CLI: Your customizable assistant for the command line interface (CLI).
"""

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel


# Constants
CHAT_LLM = "mistralai/Mistral-Nemo-Instruct-2407"
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are OpenCopilot, an advanced AI assistant designed to help you with your tasks. "
    "You are powered by MistralAI's Nemo model, which is designed to be helpful, harmless, and honest. "
    "You are also powered by the Hugging Face Hub. You can use code blocks in your responses."
    "You can also use markdown formatting in your responses.",
}


# Syntax Highlighting
def print_highlighted(code: str) -> None:
    """
    Highlight and print the provided code.

    Args:
        code (str): The code to be highlighted and printed.

    Returns:
        None
    """

    console = Console()
    md = Markdown(code, code_theme="github-dark", justify="left")

    console.print(
        Panel(
            md,
            title_align="left",
            title="[bold green]OpenCopilot[/bold green]",
        )
    )
