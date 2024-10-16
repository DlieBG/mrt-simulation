from setuptools import find_packages, setup

setup(
    name='mrt-simulation',
    version='0.1.0',
    description='',
    url='https://git.univ.leitwert.net/imprj/01-bgp-testbed/mrt-simulation',
    author='Benedikt Schwering & Sebastian Forstner',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'click',
        'pydantic',
    ],
    entry_points={
        'console_scripts': [
            'mrt-simulation=src.main:main',
        ],
    },
)
