items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]
print(items1)  # [35, 12, 99, 68, 55, 35, 87]
print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # [100, 12.3, 'Python', True]
print(type(items1))  #<class 'list'>

print(items1 + items2)

#+
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
items5 += items6
print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]

#*
print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]

#我们可以使用in或not in运算符判断一个元素在不在列表中，我们在上面的代码代码中再增加两行，如下所示。
print(45 in items6)
print(555 not in items6)


#对于反向索引，[-1]可以访问列表中的最后一个元素，[-N]可以访问第一个元素，代码如下所示。
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[-1])  # watermelon


#如果希望一次性访问列表中的多个元素，我们可以使用切片运算。
#切片运算是形如[start:end:stride]的运算符，其中start代表访问列表元素的起始位置，end代表访问列表元素的终止位置（终止位置的元素无法访问），而stride则代表了跨度，简单的说就是位置的增量，比如我们访问的第一个元素在start位置，那么第二个元素就在start + stride位置，当然start + stride要小于end。
#我们给上面的代码增加下面的语句，来使用切片运算符访问列表元素。

print(items8[1:3:1])     # ['strawberry', 'durian']
print(items8[0:3:1])     # ['apple', 'strawberry', 'durian']
print(items8[0:5:2])     # ['apple', 'durian', 'watermelon']
print(items8[-4:-2:1])   # ['strawberry', 'durian']
print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']

#如果start值等于0，那么在使用切片运算符时可以将其省略；如果end值等于N，N代表列表元素的个数，那么在使用切片运算符时可以将其省略；如果stride值等于1，那么在使用切片运算符时也可以将其省略。所以，下面的代码跟上面的代码作用完全相同。
print(items8[1:3])     # ['strawberry', 'durian']
print(items8[:3:1])    # ['apple', 'strawberry', 'durian']
print(items8[::2])     # ['apple', 'durian', 'watermelon']
print(items8[-4:-2])   # ['strawberry', 'durian']
print(items8[-2::-1])  # ['peach', 'durian', 'strawberry', 'apple']


items8[1:3] = ['x', 'o'] #修改
print(items8)  # ['apple', 'x', 'o', 'peach', 'watermelon']

#列表关系运算
nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
nums3 = [3, 2, 1]
print(nums1 == nums2)  # True
print(nums1 != nums2)  # False
print(nums1 <= nums3)  # True
print(nums2 >= nums3)  # False

#遍历
#法一
nums = [1, 2, 3, 4]
t = len(nums)
for num in range(len(nums)-1,-1,-1): #-1很关键，否则越界
    print(nums[num])

#法二

for num in nums:
    print(num)

