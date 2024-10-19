from .exabgp import check_exabgp, create_exabgp_configuration, run_exabgp
from .mrt import check_mrt2exabgp, create_python_simulation_script
from .configuration import check_configuration
from .tmp import create_tmp_path
import click, io

@click.command()
@click.option(
    '--configuration',
    '-c',
    default='/home/imprj/mrt-simulation-config.json',
    show_default=True,
    type=click.File('r'),
    help='Path to the json configuration file.',
)
@click.option(
    '--ignore-playback-speed',
    '-i',
    default=False,
    show_default=True,
    is_flag=True,
    type=bool,
    help='Ignore the playback speed of the mrt simulation.',
)
@click.argument(
    'mrt_file',
    type=click.Path(
        exists=True,
        resolve_path=True,
    ),
)
def main(mrt_file: str, configuration: io.BytesIO, ignore_playback_speed: bool):
    check_exabgp()
    check_mrt2exabgp()
    configuration = check_configuration(
        configuration=configuration.read()
    )
    tmp_path = create_tmp_path()

    python_simulation_script_path = create_python_simulation_script(
        tmp_path=tmp_path,
        mrt_file=mrt_file,
        ignore_playback_speed=ignore_playback_speed,
    )
    exabgp_configuration_path = create_exabgp_configuration(
        configuration=configuration,
        tmp_path=tmp_path,
        python_simulation_script_path=python_simulation_script_path,
    )
    run_exabgp(
        exabgp_configuration_path=exabgp_configuration_path,
    )
