from pydantic import BaseModel, ValidationError
import click, sys

class Configuration(BaseModel):
    local_ip: str
    local_as: int
    remote_ip: str
    remote_as: int

def check_configuration(configuration: str) -> Configuration:
    '''Check if a valid configuration is provided.'''

    click.echo('Checking configuration ', nl=False)

    try:
        configuration = Configuration.model_validate_json(
            json_data=configuration,
        )
        
        click.echo(click.style('ok', fg='green'))
        
        return configuration
    except ValidationError as error:
        click.echo(click.style('error', fg='red'))
        print(error)
        sys.exit(1)
