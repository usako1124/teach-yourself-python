msg = ' 　こんにちは \t\n\r'
print('「' + msg.strip() + '」') # 「こんにちは」
print('「' + msg.lstrip() + '」') # 「こんにちは \t\n\r」
print('「' + msg.rstrip() + '」') # 「 　こんにちは」

msg2 = '!======[独習Python]======!'
print('「' + msg2.strip('!=[]') + '」') # 「独習Python」