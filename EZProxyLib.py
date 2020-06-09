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
    except FileNotFoundError:
        print('Error Locating Proxies. Is your path correct?')
        quit()
    except:
        print('Error not related to path')
        quit()
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
    except FileNotFoundError:
        print('Error Locating Proxies. Is your path correct?')
        quit()
    except:
        print('Error not related to path')
        quit()

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
    except FileNotFoundError:
        print('Error Locating Proxies. Is your path correct?')
        quit()
    except:
        print('Error not related to path')
        quit()

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
        quit()
