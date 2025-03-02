"""
算术运算符

Version: 1.0
Author: 骆昊
"""
print(321 + 12)     # 加法运算，输出333
print(321 - 12)     # 减法运算，输出309
print(321 * 12)     # 乘法运算，输出3852
print(321 / 12)     # 除法运算，输出26.75
print(321 // 12)    # 整除运算，输出26
print(321 % 12)     # 求模运算，输出9
print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241



"""
算术运算的优先级

Version: 1.0
Author: 骆昊
"""
print(2 + 3 * 5)           # 17
print((2 + 3) * 5)         # 25
print((2 + 3) * 5 ** 2)    # 125
print(((2 + 3) * 5) ** 2)  # 625


"""
海象运算符

Version: 1.0
Author: 骆昊
"""
# SyntaxError: invalid syntax
# print((a = 10))
# 海象运算符 :=
print((a := 10))  # 10
print(a)          # 10


"""
比较运算 and，or，not
and 两边均真才真
or 如果两边的布尔值有任意一个是True，那么最终的结果就是True。
not运算符的后面可以跟一个布尔值，如果not后面的布尔值或表达式是True，那么运算的结果就是False；如果not后面的布尔值或表达式是False，那么运算的结果就是True。
and，or有短路处理。如and左侧为假，则不会执行后边，or左侧为真则不会执行右边。
"""

flag0 = 1 == 1
flag1 = 2 == 1
flag2 = flag0 and flag1
flag3 = flag0 or flag1
flag4 = not flag0

print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = False
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = True
print('flag4 =', flag4)     # flag4 = False


#例子：输入华氏温度将其转换为摄氏温度，华氏温度到摄氏温度的转换公式为：C = (F - 32) / 1.8
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f,c))

#格式化输出
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度') #f表示后面的字符串需要格式化处理

#计算圆周长面积
r = float(input('请输入圆的半径：'))
c = 3.14 * 2 * r
s = 3.14 * r ** 2
print(f'周长{c:.1f}')
print('%.1f周长' % c)
print(f'面积{s:.1f}')

#使用math内置模块中的pi

import math
c = math.pi * 2 * r
print(f'周长{c:.1f}')



