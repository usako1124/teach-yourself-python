import re

msg = '仕事用はwings@example.comです。'
ptn = re.compile(r'(?i)(?P<localName>[a-z0-9.!#$%&\'*+/=?^_{|}~-]+)@(?P<domain>[a-z0-9-]+(?:\.[a-z0-9-]+)*)', re.IGNORECASE)

print(ptn.sub(r'\g<domain>の\g<localName>', msg))

# 仕事用は@example.comのwingsです。
