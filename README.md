# demoMicroserviceClient
This is a demo python client to retrieve configuration of the config server

## Prerequisites
#### python modules
requests
json
yaml
#### requires a running config server (you can use mine)
Clone locally [this server](https://github.com/billatr0n/Cloud_Config_Server_Local) and fire it up using STS.
It points to [my git config repo](https://github.com/billatr0n/microservices-cloud-config)


## Installation
from a command line perform the following
```
pip install requests
pip install pyyaml
```

## Execution #1 (from the REPL)
from a command line perform the following
```
cd ~/{directory_of_the_code_you_just_cloned}
python
import client
```

## Execution #2 (from the command line)
```
cd ~/{directory_of_the_code_you_just_cloned}
python client.py
```
## Execution #3 (as a module)
With the current implementation its not supported OOTB

