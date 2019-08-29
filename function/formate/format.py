print("{} {}".format("hello", "world"))    # 不设置指定位置，按默认顺序

print("{0} {1}".format("hello", "world"))  # 设置指定位置

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

print("{:.2f}".format(3.1415926))  # 保留小数点后两位

print("{:0>2d}".format(5))  # 数字补零 (填充左边, 宽度为2)

print("{:x<4d}".format(10))  # 数字补x (填充右边, 宽度为4)

print("{:<10s}".format("11的二进制是：") + "{:b}".format(11))
print("{:<10s}".format("11的十进制是：") + "{:d}".format(11))
print("{:<10s}".format("11的八进制是：") + "{:o}".format(11))
print("{:<10s}".format("11的十六进制是：") + "{:#x}".format(11))
print("{:<10s}".format("11的十六进制是：") + "{:#X}".format(11))