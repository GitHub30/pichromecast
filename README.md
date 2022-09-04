[![Python](https://img.shields.io/pypi/pyversions/pichromecast.svg)](https://badge.fury.io/py/pichromecast)
[![PyPI](https://badge.fury.io/py/pichromecast.svg)](https://badge.fury.io/py/pichromecast)
# pichromecast
Library for MicroPython to communicate with the Google Chromecast.

## Install
`Tools` > `Manage packages...`

![Screenshot from 2022-09-04 12-42-58](https://user-images.githubusercontent.com/12811398/188297409-533b2016-d37e-4f8f-b44a-cab390adc953.png)

or copy and paste code

https://github.com/GitHub30/pichromecast/blob/main/pichromecast.py

## Usage

```python
from pichromecast import play_url

play_url('https://nyanpass.com/nyanpass.mp3', '192.168.10.101')
```

### Connect wifi and play
```python
import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("aterm-SSID-g", "YOUR_PASSWORD")
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)


from pichromecast import play_url

play_url('https://nyanpass.com/nyanpass.mp3', '192.168.10.101')
```

![image](https://user-images.githubusercontent.com/12811398/188296486-296ed2e6-84c1-493a-9125-202f22bd04cd.png)


### Lookup host IP

```python
#pip install pychromecast
import pychromecast

services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)
print(services)
[CastInfo(services={ServiceInfo(type='mdns', data='Google-Home-Mini-3b0a32dc5803130351919f8a286e406f._googlecast._tcp.local.')}, uuid=UUID('3b0a32dc-5803-1303-5191-9f8a286e406f'), model_name='Google Home Mini', friendly_name='書斎', host='192.168.10.101', port=8009, cast_type='audio', manufacturer='Google Inc.')]
```

or use [MicroPython MDNS](https://pypi.org/project/micropython-mdns/)

## Demo

[![Watch the video](https://img.youtube.com/vi/bA8fouVAPho/maxresdefault.jpg)](https://youtu.be/bA8fouVAPho)
