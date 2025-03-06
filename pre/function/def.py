"""
输入m和n，计算组合数C(m,n)的值

Version: 1.1
Author: 骆昊
"""


# 通过关键字def定义求阶乘的函数
# 自变量（参数）num是一个非负整数
# 因变量（返回值）是num的阶乘
def fac(num):
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
# 计算阶乘的时候不需要写重复的代码而是直接调用函数
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n)) #//整除


#直接调用库函数
"""
输入m和n，计算组合数C(m,n)的值

Version: 1.2
Author: 骆昊
"""
from math import factorial

m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))

"""
输入m和n，计算组合数C(m,n)的值
更改库函数名称
"""
from math import factorial as f

m = int(input('m = '))
n = int(input('n = '))
print(f(m) // f(n) // f(m - n))

# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total = 0
    # 对保存可变参数的元组进行循环遍历
    for val in args:
        # 对参数进行了类型检查（数值型的才能求和）
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())         # 0
print(add(1))        # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, 'hello', 3.45, 6))  # 12.45

# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)


"""
abs	返回一个数的绝对值，例如：abs(-1.3)会返回1.3。
bin	把一个整数转换成以'0b'开头的二进制字符串，例如：bin(123)会返回'0b1111011'。
chr	将Unicode编码转换成对应的字符，例如：chr(8364)会返回'€'。
hex	将一个整数转换成以'0x'开头的十六进制字符串，例如：hex(123)会返回'0x7b'。
input	从输入中读取一行，返回读到的字符串。
len	获取字符串、列表等的长度。
max	返回多个参数或一个可迭代对象中的最大值，例如：max(12, 95, 37)会返回95。
min	返回多个参数或一个可迭代对象中的最小值，例如：min(12, 95, 37)会返回12。
oct	把一个整数转换成以'0o'开头的八进制字符串，例如：oct(123)会返回'0o173'。
open	打开一个文件并返回文件对象。
ord	将字符转换成对应的Unicode编码，例如：ord('€')会返回8364。
pow	求幂运算，例如：pow(2, 3)会返回8；pow(2, 0.5)会返回1.4142135623730951。
print	打印输出。
range	构造一个范围序列，例如：range(100)会产生0到99的整数序列。
round	按照指定的精度对数值进行四舍五入，例如：round(1.23456, 4)会返回1.2346。
sum	对一个序列中的项从左到右进行求和运算，例如：sum(range(1, 101))会返回5050。
type	返回对象的类型，例如：type(10)会返回int；而 type('hello')会返回str。
"""