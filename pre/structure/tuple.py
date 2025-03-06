"""
元组内元素一旦定义无法更改，否则会报错

"""

tuple1 = (100,200,101)

#只有一个元素需要添加，

tuple2 = (100,)

tuple3 = tuple(range(1,6))

print(tuple3)

print(tuple1 + tuple2)

#打包和解包

a = 10
b = 20

m, n = 10, 20
tuple4 = (10,20)
p, q = tuple4

#如果存在一对多

tuple5 = (range(1,11))
x,y,*z = tuple5
print(x,y,z) #1 2 [3, 4, 5, 6, 7, 8, 9, 10]

x,*y,z = tuple5
print(x,y,z)

#交换变量
a,b = b,a

#可与列表转换
tuple6 = (range(1,6))
print(list(tuple6))


