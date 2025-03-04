print(0b100)  # 二进制整数
print(0o100)  # 八进制整数
print(100)    # 十进制整数
print(0x100)  # 十六进制整数


print(123.456)    # 数学写法
print(1.23456e2)  # 科学计数法



a = 10
b = 20
print(a + b)


"""
使用type函数检查变量的类型
"""
a = 100
b = 123.45
c = 'hello, world'
d = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>


#强制转换
a = '123'
b = '100'
print(int(a))
print(int(b,base = 2)) #以二进制转为int输出


"""
变量的类型转换操作

Version: 1.0
Author: 骆昊
"""
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(c))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出123.45
print(bool(f))          # str类型的'hello, world'转成bool，输出True
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd'
print(ord('d'))         # str类型的'd'转成int，输出100