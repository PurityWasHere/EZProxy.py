# EzProxyLib
A very easy way to load and select proxies. 

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

Step 1) Put this file in the same folder as your project, or load it as a library

Step 2) Call the function you want ex: GrabProxiesHTTP('proxies.txt') < If the proxies.txt file is in your local folder.

Step 3) Call RefreshProxy() Every time you want a new proxy to be used. Make sure to do step 2 first to propigate the proxies list.

Thats all. Have Fun having easy access to proxies while keeping your code clean.

To Load a Library:

Step 1) Create a folder named "Lib" in your projects directory.

Step 2) Create a file named __init__.py inside of the Lib Folder

Step 3) Put EzProxyLib.py inside of the Lib folder.

Step 4) import to your python script using from lib import EzProxyLib
