# EzProxy.py

<p align="center">
  <img width="171‬" height="102" src="https://i.imgur.com/c71GUHG.png">
</p>

A very easy way to load and select proxies. Load proxies in 3 lines!
<p>Example for Http Proxies:</p>

```python
from lib import EZProxy as ProxyManager
ProxyManager.GrabProxiesHTTP('http_proxies.txt')
ProxyManager.RefreshProxy()
print(ProxyManager.http)
>>>{'http': 'http://xxx.xxx.xx.xx:8080', 'https': 'https://xxx.xxx.xx.xx:8080'}
```

Quick Usage:

Step 1) Create a folder called lib in the same directory as your project

Step 2) Create a file inside of the Lib folder called _init\_.py, Place EZProxy.py inside

step 3) add this to the top line of your project 'from lib import EZProxy'

Step 4) Call the function you want ex: GrabProxiesHTTP('proxies.txt') < If the proxies.txt file is in your local folder.

Step 5) Call RefreshProxy() Every time you want a new proxy to be used. Make sure to do step 2 first to propigate the proxies list.


