import re

msg = '住所は〒160-0000 新宿区南町0-0-0です。\nあなたの住所は〒210-9999 川崎市北町1-1-1'
ptn = re.compile(r'〒\d{3}-\d{4}')
results = ptn.findall(msg)
for result in results:
    print(result)


msg2 = 'お問い合わせはsupport@example.comまで'
ptn = re.compile(r'([a-z0-9.!#$%&\'*+/=?^_{|}~-]+)@([a-z0-9-]+(?:\.[a-z0-9-]+)*)', re.IGNORECASE)
result = ptn.sub(r'<a href="mailto:\g<0>">\g<0></a>', msg2)
print(result)

