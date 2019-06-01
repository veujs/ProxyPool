import requests
from proxypool.setting import TEST_URL

proxy = '96.9.90.90:8080'


benji_yrl = "http://0.0.0.0:5555/random"
response = requests.get(benji_yrl, verify=False)
print(response.text)
proxy = response.text
print(proxy)
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
print(proxies)


print(TEST_URL)
response = requests.get(TEST_URL, proxies=proxies, verify=False)
if response.status_code == 200:
    print('Successfully')
    print(response.text)
else:
    print("123")
    print(response.status_code)

