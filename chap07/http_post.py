import requests

res = requests.post('https://usacode.xsrv.jp/study/python/post.php', data={'name', '佐々木新之助'})
print(res.text)