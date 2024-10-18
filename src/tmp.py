from pathlib import Path
import click

def create_tmp_path() -> Path:
    '''Create temporary path for exabgp configuration and python simulation script.'''
    click.echo('Creating temporary path ', nl=False)
    
    tmp_path = Path('.mrt-simulation')
    tmp_path.mkdir(exist_ok=True)

    click.echo(click.style('ok', fg='green'))

    return tmp_path
