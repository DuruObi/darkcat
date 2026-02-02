import os
import click
import importlib
import pkgutil

from darkcat.commands.test import test
from darkcat.commands.lint import lint
from darkcat.commands.build import build
from darkcat.commands.deploy import deploy
from darkcat.commands.update import update
from darkcat.version import __version__
from darkcat.commands.init import init
from darkcat.commands.add import add
from darkcat.commands.doctor import doctor
from darkcat.commands.wizard import wizard
from darkcat.config import load_config

# Load user config (optional)
config = load_config()

# Root CLI group
@click.group()
@click.version_option(__version__, prog_name="DarkCat", message="%(prog)s version %(version)s")
def cli():
    """🐈‍⬛ DarkCat — Developer Automation Tool"""
    pass

# Core commands
cli.add_command(test)
cli.add_command(lint)
cli.add_command(build)
cli.add_command(deploy)
cli.add_command(update)
cli.add_command(init)
cli.add_command(add)
cli.add_command(doctor)
cli.add_command(wizard)

# Plugin system: load commands dynamically from plugins folder
PLUGINS_PATH = os.path.join(os.path.dirname(__file__), "plugins")

if os.path.exists(PLUGINS_PATH):
    for finder, name, ispkg in pkgutil.iter_modules([PLUGINS_PATH]):
        module = importlib.import_module(f"darkcat.plugins.{name}")
        if hasattr(module, "cli_command"):
            cli.add_command(module.cli_command)

# CLI entry point
if __name__ == "__main__":
    cli()
