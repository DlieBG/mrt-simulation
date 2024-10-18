# mrt-simulation

## Installation
To get started with the installation of `mrt-simulation`, first clone the git repo.
```
git clone https://git.univ.leitwert.net/imprj/01-bgp-testbed/mrt-simulation
cd mrt-simulation
```
After that you can install the package locally on your machine using `pip`.
```
pip3 install --break-system-packages -e .
```
Besides that you will also need to have a installation of exabgp and mrtparse.\
On Debian based systems you can use `apt`.
```
sudo apt install -y exabgp mrtparse
```

## Configuration
The configuration of the tool is done by providing a json file.\
The default path for this file is `/home/imprj/mrt-simulation-config.json`.\
To change the configuration path you can use the cli options `--configuration` or `-c`.\
The configuration json has to provide the following fields depending on your usecase:
```json
{
    "local_ip": "172.17.179.104",
    "local_as": 1,
    "remote_ip": "172.17.179.103",
    "remote_as": 1
}
```

## Usage
The usage of this tool is very simple.\
Just type `mrt-simulation` followed by the mrt file you want to simulate.
```
mrt-simulation 20241005_2345_1728171900_bgp_lw_ixp_decix_update
```
Keep in mind that the directory `.mrt-simulation` will be created to store temporary files.
