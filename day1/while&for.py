#Fibonacci
a,b = 0,1
for _ in range(20):
    a,b = b,a+b
    print(a)

#serch number
for i in range(100,1000):
    low = i % 100
    mid = i // 10 % 10 #//整除
    high = i // 100
    if low ** 3 + mid ** 3 + high ** 3 == i:
        print(i)



