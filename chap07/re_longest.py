import re

tags = '<p><strong>WINGS</strong>サイト<a href="index.html"><img src="wings.jpg" /></a></p>'
ptn = re.compile(r'<.+?>')
results = ptn.findall(tags)
for result in results:
    print(result)

# <p>
# <strong>
# </strong>
# <a href="index.html">
# <img src="wings.jpg" />
# </a>
# </p>