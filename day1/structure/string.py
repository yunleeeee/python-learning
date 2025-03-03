#转义字符
#例如要输出一个带单引号或反斜杠的字符串，需要用如下所示的方法。
s1 = '\'hello, world!\''
s2 = '\\hello, world!\\'
print(s1)
print(s2)

#原始字符串 r
s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)

#字符串计算
#拼接和重复
s1 = 'hello' + ', ' + 'world'
print(s1)    # hello, world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2
print(s1)    # hello, world!!!
s1 *= 2
print(s1)    # hello, world!!!hello, world!!!
#比较运算

s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)             # False
print(s1 < s2)              # True
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
s3 = '骆昊'
print(ord('骆'))            # 39558
print(ord('昊'))            # 26122
s4 = '王大锤'
print(ord('王'))            # 29579
print(ord('大'))            # 22823
print(ord('锤'))            # 38180
print(s3 >= s4)             # True
print(s3 != s4)             # True

#成员运算 in， not in
s1 = '李昀卓'
print('李' in s1)           #True
print('a' not in s1)       #True

#len获取长度
#索引和切片
s = 'hello, world'
print(len(s))                 # 12
print(len('goodbye, world'))  # 14

s = 'abc123456'
n = len(s)
print(s[0], s[-n])    # a a
print(s[n-1], s[-1])  # 6 6
print(s[2], s[-7])    # c c
print(s[5], s[-4])    # 3 3
print(s[2:5])         # c12
print(s[-7:-4])       # c12
print(s[2:])          # c123456
print(s[:2])          # ab
print(s[::2])         # ac246
print(s[::-1])        # 654321cba

#字符串是不可变类型
#对于字符串foo，有方法bar，我们使用foo.bar来使用方法
#大小写转换，但不改变原本字符串
s1 = 'hello, world!'
# 字符串首字母大写
print(s1.capitalize())  # Hello, world!
# 字符串每个单词首字母大写
print(s1.title())       # Hello, World!
# 字符串变大写
print(s1.upper())       # HELLO, WORLD!
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())       # goodbye
# 检查s1和s2的值
print(s1)               # hello, world
print(s2)               # GOODBYE

s = '李昀卓'
a = list(s)
print(a)

#遍历
s = '1029180'
for i in s:
    print(i)

for i in range(len(s)):
    print(s[i])

#查找 find，index
s = '102901'
print(s.find('1'))    #0 只能找一个
print(s.find('10',2))    #-1
print(s.index('10'))    #0
print(s.index('1'))    #0
print(s.index('11',6))    #ValueError: substring not found

#逆向查找 rfind,rindex

#性质判断

s1 = 'hello, world!'
print(s1.startswith('He'))   # False
print(s1.startswith('hel'))  # True
print(s1.endswith('!'))      # True
s2 = 'abc123456'
print(s2.isdigit())  # False 纯数字
print(s2.isalpha())  # False 纯字母
print(s2.isalnum())  # True 是否是数字加字母

#格式化
s = 'hello, world'
print(s.center(20, '*'))  # ****hello, world****  居中
print(s.rjust(20))        #         hello, world 右对齐
print(s.ljust(20, '~'))   # hello, world~~~~~~~~ 左对齐
print('33'.zfill(5))      # 00033 左边补0
print('-33'.zfill(5))     # -0033

#修建 strip 默认修建空格
s1 = '   jackfrued@126.com  '
print(s1.strip())      # jackfrued@126.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  # 你好，世界~
print(s2.rstrip('~'))  # ~你好，世界
#replace
s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 1))  # hell@, good world

#拆分与合并
s = 'I love you'
words = s.split()
print(words)            # ['I', 'love', 'you'] 列表 默认空格拆分
print('~'.join(words))  # I~love~you

s = 'I#love#you#so#much'
words = s.split('#')
print(words)  # ['I', 'love', 'you', 'so', 'much']
words = s.split('#', 2)
print(words)  # ['I', 'love', 'you#so#much']


