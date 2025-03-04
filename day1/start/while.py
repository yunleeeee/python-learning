total = 100
i = 1
while i <= 100:
    total += i;
    i += 1
print(total)

"""
从1到100的偶数求和

Version: 1.4
Author: 骆昊
"""
total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)


"""
从1到100的偶数求和

Version: 1.5
Author: 骆昊
"""
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    total += i
print(total)