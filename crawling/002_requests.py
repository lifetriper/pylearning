import requests

url = "https://www.sogou.com/web?query=周杰伦"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/101.0.4951.64 Safari/537.36"
}

resp = requests.get(url, headers=headers)
print(resp)
print(resp.request)
print(resp.text)
