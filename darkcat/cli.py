import click

# 1️⃣ Import all command modules
from darkcat.commands.init import init
from darkcat.commands.add import add
from darkcat.commands.doctor import doctor
from darkcat.commands.wizard import wizard  # wizard imported here

# 2️⃣ Define main CLI group
@click.group()
def cli():
    """🐈‍⬛ DarkCat — Developer Automation Tool"""
    pass

# 3️⃣ Add commands to CLI
cli.add_command(init)
cli.add_command(add)
cli.add_command(doctor)
cli.add_command(wizard)  # add wizard here, AFTER cli is defined

# 4️⃣ Entry point
if __name__ == "__main__":
    cli()
