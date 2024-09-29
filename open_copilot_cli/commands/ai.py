""" Command to ask questions """

from typing import Annotated
import typer
from huggingface_hub import InferenceClient
from rich import print
from open_copilot_cli import CHAT_LLM, SYSTEM_MESSAGE, print_highlighted


def ai(
    prompt: Annotated[str, typer.Argument(help="Natural language prompt.")],
    model: Annotated[
        str,
        typer.Option(
            "--model",
            "-m",
            help="The model to run inference with. Can be a model id hosted on the "
            "Hugging Face Hub, e.g. meta-llama/Meta-Llama-3-8B-Instruct or a URL "
            "to a deployed Inference Endpoint.",
        ),
    ] = CHAT_LLM,
) -> None:
    """
    Ask questions using the specified language model. The model can be a model id hosted on
    the Hugging Face Hub, e.g. meta-llama/Meta-Llama-3-8B-Instruct or a URL to a deployed
    Inference Endpoint.

    Args:
        prompt (str): The natural language prompt from which to generate a command.
    """

    client = InferenceClient(model)

    try:
        response = client.chat_completion(
            messages=[SYSTEM_MESSAGE, {"role": "user", "content": prompt}],
            max_tokens=1024,
        )

        print_highlighted(response.choices[0].message.content)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
