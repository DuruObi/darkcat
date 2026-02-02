import click, subprocess

@click.command()
def update():
    '''Update DarkCat to latest version'''
    click.echo('🐈‍⬛ Updating DarkCat ...')
    subprocess.run(['pip','install','--upgrade','darkcat'])
