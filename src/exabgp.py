from .configuration import Configuration
import subprocess, click, sys, os
from pathlib import Path

def check_exabgp():
    '''Check if exabgp is installed on the system.'''

    click.echo('Checking exabgp ', nl=False)
    
    if os.path.exists('/usr/sbin/exabgp'):
        click.echo(click.style('ok', fg='green'))
    else:
        click.echo(click.style('error', fg='red'))
        sys.exit(1)

def create_exabgp_configuration(
    configuration: Configuration,
    tmp_path: Path,
    python_simulation_script_path: Path,
) -> Path:
    '''Create temporary exabgp configuration depending on previously parsed configuration.'''
    
    exabgp_configuration_path = tmp_path.joinpath('exabgp.conf')
    exabgp_configuration_path.write_text(
        data=f'''neighbor {configuration.remote_ip} {{
    router-id {configuration.local_ip};
    local-address {configuration.local_ip};
    local-as {configuration.local_as};
    peer-as {configuration.remote_as};
    hold-time 180;

    api {{
        processes [mrt-simulation];
        send {{
            packets;
        }}
    }}
}}

process mrt-simulation {{
    run python3 {python_simulation_script_path.absolute()};
    encoder text;
}}''',
    )

    return exabgp_configuration_path

def run_exabgp(exabgp_configuration_path: Path):
    '''Run exabgp with previously created configuration.'''

    subprocess.run(
        args=[
            'sudo',
            'exabgp',
            exabgp_configuration_path.absolute(),
        ],
        stderr=sys.stderr,
        stdout=sys.stdout,
    )
