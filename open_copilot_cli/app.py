""" OpenCopilot CLI """

import typer
from open_copilot_cli.commands import command_list


# CLI
open_copilot = typer.Typer(
    name="code-pilot",
    no_args_is_help=True,
    rich_markup_mode="rich",
    help="OpenCopilot CLI, an advanced AI-powered customizable assistant.",
)

for command in command_list:
    open_copilot.command(no_args_is_help=True)(command)


if __name__ == "__main__":
    open_copilot()
