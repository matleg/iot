# IoT

## Installation

Counterfit

```sh
python3.9 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip


pip install counterFit
pip install counterfit-connection
pip install counterfit-shims-grove
pip install counterfit-shims-seeed-python-dht

pip uninstall -y Werkzeug && pip install Werkzeug==2.3.6

# start with command line:
counterfit
```

## check mosquitto docker

```sh
docker exec -it addon_core_mosquitto bash

root@core-mosquitto:/# mosquitto_sub -h localhost -u mqtt_user -P mqtt_password -t '#' -v
# -h host
# -t topic ('#': all)


# purge all messages
root@core-mosquitto:/# mosquitto_sub -h localhost -u mqtt_user -P mqtt_password --remove-retained -t '#' -W 1

```
