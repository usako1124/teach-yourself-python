data = ['こんにちは', 'おはよう', 'おやすみ']
keywd = {'sep': ',', 'end': '●'}
print(*data, **keywd)  # こんにちは,おはよう,おやすみ●
