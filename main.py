import requests
import time
import json
import os


requests.packages.urllib3.disable_warnings()
cookie = os.getenv('COOKIE')
assert cookie

headers = {
    'Host': 'gw.aikan.miguvideo.com',
    'Accept': '*/*',
    'hwcookie': 'undefined',
    'EpgSession': 'JSESSIONID=0236IYD2HOSLAB66KZ5K311IW8D7PD9T',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate, br',
    'Location': 'http://vsc.aikan.miguvideo.com7128',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://gw.aikan.miguvideo.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 miguaikan',
    'Referer': 'https://gw.aikan.miguvideo.com/h5-agg/center/1/index.html',
    'Content-Length': '0',
    'Connection': 'keep-alive',
    'Cookie': cookie
}


try:
    text = requests.post(url='https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-sign/sign', headers=headers,
                         verify=False).text
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), text)
except:
    pass

