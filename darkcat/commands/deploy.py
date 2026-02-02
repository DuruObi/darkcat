import click

@click.command()
@click.option('--folder', default='.', help='Project folder')
@click.option('--target', default='staging', help='Deployment target')
def deploy(folder,target):
    '''Deploy project to target'''
    click.echo(f"🐈‍⬛ Deploying {folder} to {target} ...")
    click.echo('✅ Deployment simulation complete')
