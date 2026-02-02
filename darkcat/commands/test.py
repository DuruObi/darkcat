import click, subprocess, os

@click.command()
@click.option('--folder', default='.', help='Project folder')
def test(folder):
    '''Run project test suites'''
    click.echo(f"🐈‍⬛ Running tests in {folder} ...")
    if os.path.exists(os.path.join(folder, 'package.json')):
        subprocess.run(['npm','test'], cwd=folder)
    elif os.path.exists(os.path.join(folder, 'pyproject.toml')) or os.path.exists(os.path.join(folder,'setup.py')):
        subprocess.run(['pytest'], cwd=folder)
    else:
        click.echo('⚠️ No recognizable test framework found!')
