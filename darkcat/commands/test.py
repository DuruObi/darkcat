import click
import subprocess
import os

@click.command()
@click.option("--folder", default=".", help="Project folder")
def test(folder):
    """Run Python test suites only"""
    click.echo(f"🐈‍⬛ Running Python tests in {folder} ...")
    if os.path.exists(os.path.join(folder, "tests")):
        subprocess.run(["pytest", os.path.join(folder, "tests")])
    else:
        click.echo("⚠️ No Python tests found!")
