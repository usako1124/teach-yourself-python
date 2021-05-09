title = ['部長', '課長', '係長', '主任']
data = [
    {'name': '山田太郎', 'position': '主任'},
    {'name': '鈴木次郎', 'position': '部長'},
    {'name': '田中花子', 'position': '課長'},
    {'name': '佐野恵子', 'position': '係長'},
]

data.sort(key=lambda x: title.index(x['position']))
print(data)
# [
#     {'name': '鈴木次郎', 'position': '部長'},
#     {'name': '田中花子', 'position': '課長'},
#     {'name': '佐野恵子', 'position': '係長'},
#     {'name': '山田太郎', 'position': '主任'},
# ]
