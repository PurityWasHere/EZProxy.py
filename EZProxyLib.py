'''
EZProxyLib is a Easy to Use Proxy loading lib for easily loading Http/Https Proxies, Aswell as Socks4/Socks5 Proxies.

How To Use
---------------
Step 1) Put this file in the same folder as your project, or load it as a library
Step 2) Call the function you want ex: GrabProxiesHTTP('proxies.txt') < If the proxies.txt file is in your local folder.
Step 3) Call RefreshProxy() Every time you want a new proxy to be used. Make sure to do step 2 first to propigate the proxies list.
Thats all. Have Fun having easy access to proxies while keeping your code clean.
'''

import random
proxyCount = 0
proxies = []
IP = ''
http = {'http':'http://' + IP,
        'https':'https://' + IP}
socks4 = {'http':'socks4://' + IP,
          'https':'socks4://' + IP}
socks5 = {'http':'socks5://' + IP,
          'https':'socks5://' + IP}


def GrabProxiesHTTP(ProxyPath):
    try:
        global proxyCount
        global proxies
        with open(ProxyPath, 'r') as f:
            for line in f:
                stripped = line.replace('\n','')
                proxies.append(stripped)
        for line in proxies:
            proxyCount+=1
        return proxyCount
        return proxies
    except:
        print('Error Loading Proxies. Is proxies.txt in the local Directory?')

def GrabProxiesSOCKS4(ProxyPath):
    try:
        global proxyCount
        global proxies
        with open(ProxyPath, 'r') as f:
            for line in f:
                stripped = line.replace('\n','')
                proxies.append(stripped)
        for line in proxies:
            proxyCount+=1
        return proxyCount
        return proxies
    except:
        print('Error Loading Proxies. Is proxies.txt in the local Directory?')

def GrabProxiesSOCKS5(ProxyPath):
    try:
        global proxyCount
        global proxies
        with open(ProxyPath, 'r') as f:
            for line in f:
                stripped = line.replace('\n','')
                proxies.append(stripped)
        for line in proxies:
            proxyCount+=1
        return proxyCount
        return proxies
    except:
        print('Error Loading Proxies. Is proxies.txt in the local Directory?')

def RefreshProxy():
    try:
        global proxies
        global http
        global socks4
        global socks5
        global IP
        IP = random.choice(proxies)
        http = {'http':'http://' + IP,
                'https':'https://' + IP}
        socks4 = {'http':'socks4://' + IP,
                  'https':'socks4://' + IP}
        socks5 = {'http':'socks5://' + IP,
                  'https':'socks5://' + IP}
        return http
        return socks4
        return socks5
    except:
        print('Error Refreshing Proxies. Did you run GrabProxies<Type> Before running this?')

