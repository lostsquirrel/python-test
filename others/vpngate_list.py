__author__ = 'lisong'

import requests

url = "http://www.vpngate.net/api/iphone/"
proxies = {
    'http': 'http://127.0.0.1:8087',
    'https': 'http://127.0.0.1:8087',
}

res = requests.get(url, proxies=proxies);
print(res)
print(res.content)