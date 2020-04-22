# MoistureSensor

install Raspbian: https://www.raspberrypi.org/downloads/raspbian/

enable SSH for Headless connection:
- Add a file named `ssh` to boot directory from another computer.
- login via: ssh pi@IP.address
- password: raspberry

## Setup Circuit Python
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install vim
$ sudo pip3 install --upgrade setuptools
$ pip3 install adafruit-blinka
$ pip3 install RPI.GPIO
```

Enable I2C
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
```
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools
sudo raspi-config
```
Follow prompts
- Interfacing Options
- P5 I2C
- P4 SPI  # Not needed now, but why not

```
sudo reboot
```

Test Setup
```
$ sudo i2cdetect -y 1

pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- 36 -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
pi@raspberrypi:~ $ ls /dev/i2c* /dev/spi*
/dev/i2c-1  /dev/spidev0.0  /dev/spidev0.1

pi@raspberrypi:~/Documents $ python3 ~/Documents/blinkatest.py
Hello blinka!
Digital IO ok!
I2C ok!
SPI ok!
done!
```

Install seesaw Library
`sudo pip3 install adafruit-circuitpython-seesaw`



## AWS IOT
https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-raspi-setup.html

- logged in with AIM user banksd (754972070574)
- Created AWS_IOT_Policy
- Created Single Thing: `RaspberryPiPOC01`

```
openssl base64 -in <in file> -out <out file>
```

Add AWS Library
```
pip3 install AWSIoTPythonSDK
```

endpoint = iot.us-west-2.amazonaws.com
https://iotevents.us-west-2.amazonaws.com/things/RaspberryPiPOC01/shadow

account-specific-prefix-ats.iot.region.amazonaws.com
https://data.iot.us-west-2.amazonaws.com/things/RaspberryPiPOC01/shadow
a35bkr5k4djq7a-ats.iot.us-west-2.amazonaws.com

Endpoint is here: https://us-west-2.console.aws.amazon.com/iot/home?region=us-west-2#/thing/RaspberryPiPOC01

```
python3 moistureSensor.py --endpoint a35bkr5k4djq7a-ats.iot.us-west-2.amazonaws.com --rootCA ~/certs/AmazonRootCA1.pem --cert ~/certs/55328ae906-certificate.pem.crt --key ~/certs/55328ae906-private.pem.key --thingName RaspberryPiPOC01 --clientId RaspberryPiPOC01

python3 /home/pi/Documents/MostureProbe/moistureSensor.py --endpoint a35bkr5k4djq7a-ats.iot.us-west-2.amazonaws.com --rootCA ~/certs/AmazonRootCA1.pem --cert ~/certs/668db68b92-certificate.pem.crt --key ~/certs/668db68b92-private.pem.key --thingName RaspberryPiPOC01 --clientId RaspberryPiPOC01
```

- [ ] Had to create a genaric AWS IOT policy for the keys to work.
https://github.com/aws/aws-iot-device-sdk-python/issues/154
- [ ] MoistureSensorPolicy2: https://us-west-2.console.aws.amazon.com/iot/home?region=us-west-2#/policy/MoistureSensorPolicy2

## WiFi Setup
https://learn.adafruit.com/raspberry-pi-zero-creation/text-file-editing

- [ ] This one: https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
