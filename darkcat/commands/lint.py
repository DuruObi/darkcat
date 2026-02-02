import click, subprocess, os

@click.command()
@click.option('--folder', default='.', help='Project folder')
def lint(folder):
    '''Run linters'''
    click.echo(f"🐈‍⬛ Running linter in {folder} ...")
    if os.path.exists(os.path.join(folder,'package.json')):
        subprocess.run(['npx','eslint','.'], cwd=folder)
    elif os.path.exists(os.path.join(folder,'pyproject.toml')) or os.path.exists(os.path.join(folder,'setup.py')):
        subprocess.run(['flake8', folder])
    else:
        click.echo('⚠️ No recognizable lint setup found!')
