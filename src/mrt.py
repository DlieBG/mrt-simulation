import subprocess, click, sys, os
from pathlib import Path

def check_mrt2exabgp():
    '''Check if mrt2exabgp is installed on the system.'''

    click.echo('Checking mrt2exabgp ', nl=False)
    
    if os.path.exists('/usr/bin/mrt2exabgp'):
        click.echo(click.style('ok', fg='green'))
    else:
        click.echo(click.style('error', fg='red'))
        sys.exit(1)

def create_python_simulation_script(tmp_path: Path, mrt_file: str) -> Path:
    '''Create python simulation script and write output to temporary file.'''

    python_simulation_script = subprocess.run(
        args=[
            'mrt2exabgp',
            '-G', # convert to ExaBGP API format and group updates with the same attributes for each spceified the number of prefixes using "announce attributes ..." syntax
            '-A', # convert to ExaBGP API format
            '-P', # convert to ExaBGP API program
            mrt_file,
        ],
        capture_output=True,
        text=True,
    )

    python_simulation_script_path = tmp_path.joinpath('simulation.py')
    python_simulation_script_path.write_text(
        data=python_simulation_script.stdout,
    )

    return python_simulation_script_path
