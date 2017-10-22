# coding=utf-8

foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]

# print sorted(foo, key=lambda x: (x >= 0 and -abs(1/float(x+1)) or abs(x)))

print sorted(foo, key=lambda x: - 1.0 / (x + 1) if x >= 0 else -x)
