"""
每隔1秒输出一次“hello, world”，持续1小时

Author: 骆昊
Version: 1.0
"""
import time

for i in range(3600):
    print('hello, world')
    time.sleep(1)

"""
range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于是左闭右开的设定，即[1, 101)。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到。
"""

"""
每隔1秒输出一次“hello, world”，持续1小时

Author: 骆昊
Version: 1.1
"""
import time

for _ in range(3600): #对于不需要用到循环变量的for-in循环结构，按照 Python 的编程惯例，我们通常把循环变量命名为_
    print('hello, world')
    time.sleep(1)


"""
从1到100的整数求和

Version: 1.0
Author: 骆昊
"""
total = 0
for i in range(1, 101):
    total += i
print(total)


total = 0
for i in range(0,101,2):
    total += i
print(total)

print(sum(range(2, 101, 2)))