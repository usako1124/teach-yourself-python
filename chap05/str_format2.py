print('{0:>10}'.format('wings'))  # '     wings'
print('{0:*>10}'.format('wings'))  # '*****wings'
print('{0:0=10}'.format(-12345))  # -000012345
print('{0:,}'.format(9876543210))  # 9,876,543,210
print('{0:#_x}'.format(0x5f5bce1aa))  # 0x5_f5bc_e1aa
print('{0:.1f}cm'.format(5))  # 5.0cm
print('{0:.4g}g'.format(22.567))  # 22.57g
print('{0:x}'.format(255))  # ff
print('{0:X}'.format(255))  # FF
print('{0:.2%}'.format(0.12345))  # 12.35%
