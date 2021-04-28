while True:
    try:
        num = input('入力してください。')
        print('2倍すると...', float(num) * 2)
    except ValueError as ex:
        print('エラー発生:', ex)
    else:
        break