import click, subprocess

@click.command()
@click.option('--folder', default='.', help='Project folder')
def build(folder):
    '''Build project artifacts'''
    click.echo(f"🐈‍⬛ Building project in {folder} ...")
    subprocess.run(['python','setup.py','sdist','bdist_wheel'], cwd=folder)
