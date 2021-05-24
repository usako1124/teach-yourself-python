import requests

res = requests.post('https://usacode.xsrv.jp/post.php', data={'name', '佐々木新之助'})
print(res.text)