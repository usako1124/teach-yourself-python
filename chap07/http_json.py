import requests

res = requests.get('https://usacode.xsrv.jp/study/python/books.json')
bs = res.json()
print(bs['books'][0]['title'])
