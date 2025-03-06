lists = ['python','c','java']

#append 追加

lists.append('javascript')

#insert 插入

lists.insert(1,'SQL')

#remove 删除

if 'java' in lists:
    lists.remove('java')

#pop 默认删除最后一个

lists.pop()
q = lists.pop()

#clear 清空

lists.clear()

#del 删除

del lists[1]


items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))     # 0
# 从索引位置1开始查找'Python'
print(items.index('Python', 1))  # 5
print(items.count('Python'))     # 2
print(items.count('Kotlin'))     # 1
print(items.count('Swfit'))      # 0
# 从索引位置3开始查找'Java'
print(items.index('Java', 3))    # ValueError: 'Java' is not in list


#列表的sort操作可以实现列表元素的排序，而reverse操作可以实现元素的反转，代码如下所示。
items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items.sort()
print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
items.reverse()
print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']



#列表生成
#原本
items = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)
#列表生成
items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)


nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    nums2.append(num ** 2)
print(nums2)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)


#嵌套数组

scores = []
for _ in range(5):
    temp = []
    for _ in range(3):
        score = int(input('请输入: '))
        temp.append(score)
    scores.append(temp)
print(scores)

import random

scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)