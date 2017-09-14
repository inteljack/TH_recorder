# TH_recorder

## Envirnment
* Linux raspberrypi 4.9.41
* Python 2.7x

## To setup Python script as daemon to run on RPi3 boot-up
* Place threc.service file under /lib/systemd/system
* Run the following commands:
`sudo chmod 644 /lib/systemd/system/hello.service`
`sudo chmod +x (your script dir)/hello_world.py`
* Edit crontab to execute command after boot
`sudo crontab -e`
* Add following lines in the end:
@reboot /usr/bin/pigpiod
@reboot /usr/bin/service threc start

