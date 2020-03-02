# EzProxyLib
A very easy way to load and select proxies. Load proxies in 3 lines!

Example for Http Proxies: 
```python
from lib import EZProxyLib
import requests
EZProxyLib.GrabProxiesHTTP('proxies.txt')
EZProxyLib.RefreshProxy()
sesh = requests.get('https://Example.com',proxies = EZProxyLib.http)
print(sesh.status_code)
print(EZProxyLib.http)
>>> 200
>>> {'http': 'http://IP', 'https': 'https://IP'}
```

Quick Usage:

Step 1) Create a folder called lib in the same directory as your project

Step 2) Create a file inside of the Lib folder called init.py, Place EZProxyLib.py inside

step 3) add this to the top line of your project 'from lib import EZProxyLib'

Step 4) Call the function you want ex: GrabProxiesHTTP('proxies.txt') < If the proxies.txt file is in your local folder.

Step 5) Call RefreshProxy() Every time you want a new proxy to be used. Make sure to do step 2 first to propigate the proxies list.

Thats all. Have Fun having easy access to proxies while keeping your code clean.

