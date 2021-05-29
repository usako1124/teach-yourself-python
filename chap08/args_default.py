def get_triangle(base=5, height=1):
    return base * height / 2

print(f'三角形の面積は{get_triangle()}です')  # 2.5
print(f'三角形の面積は{get_triangle(10)}です')  # 5.0
print(f'三角形の面積は{get_triangle(10, 5)}です')  # 25,0
