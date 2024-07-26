# ESPHOME

Install ESPHOME <https://www.home-assistant.io/integrations/esphome>.

## Create yaml file

Use template for corresponding µ-controler & sensor [documentation](https://devices.esphome.io/) to create the `yaml` file.

C++ code will be generated from the yaml file when `install` is clicked, and then compiled into a `.bin`.

## Upload to device

Upload this `.bin` file to the sensor, using <https://web.esphome.io/> first (use chromium), and then OTA (OnTheAir) once the wifi info is configured and device is connected .
