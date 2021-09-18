# Async Traffic Bot
I wrote this programme just for fun. It's async programme for rising website traffic.
## How it work
The script will generate random header, screen resolution, referrer and geolocation (need proxies). After going to site, bot will be try to get all links on the page and follow to the received random link, it can be  repeated from 2 to 5 times.
## Requirements
* Chromium based browser
* [python 3.7+](https://www.python.org/)
* ```pip install -r requirements.txt```
## Using
```python
from rate_up import RateUp

app = RateUp()

# how long bot will be on page (optional)
app.min_time = 40 # default 62 sec
app.max_time = 120 # default 146 sec

app.browser_path = 'full_path_to\chrome.exe'

# generate headers list
headers = app.generate_header_list(2000)

# path to your proxy file (need pass one or more files)
proxy_list = app.get_proxy(
    socks5=r'path_to\socks5.txt',
    socks4=r'path_to\socks4.txt',
    http=r'path_to\http_https.txt',
    unknown=r'path_to\unknown_protocol.txt'
)
print(proxy_list)

# target urls list
urls = [
    'http://example.com',
    'http://example.com/index/article/0-5',
]

app.start(proxy_list, headers, urls)
```
if you want using your own referrer list or expand the existing:
```python
from rate_up import RateUp

app = RateUp()

# for new list
app.change_referrer(new='site-1.com, site-2.com')

# for expand list
app.change_referrer(expand='site-1.com, site-2.com')

# show the list what is using to generate the header (referrer, cache_control, accept, accept_encoding, user_agent)
app.show_header_data('referrer')
```
## Donate
If you want, you can [support](https://destream.net/live/iterweb/donate) me!
## Additional tools (if you need)
* [Proxy Grabber](https://github.com/iterweb/proxy_grabber)
* [Proxy Checker](https://github.com/iterweb/proxy_checker)

***I am not responsible for the use of this script!***
