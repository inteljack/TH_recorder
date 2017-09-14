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

* Copy the init script (.sh file) into "/etc/init.d"


### References

https://www.google.com.tw/url?sa=t&rct=j&q=&esrc=s&source=web&cd=8&cad=rja&uact=8&ved=0ahUKEwi9-ryb_aTWAhUBkJQKHcevAEAQtwIIQzAH&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DIHTnU1T8ETk&usg=AFQjCNG7OdfCElFi89S3gbxa6JfAu-tTNQ

http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie

http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/
