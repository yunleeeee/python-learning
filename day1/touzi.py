import random

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0

for i in range(0,6000):
    p = random.randrange(1,7)
    if p == 1:
        sum1 += 1
    elif p == 2:
        sum2 += 1
    elif p == 3:
        sum3 += 1
    elif p == 4:
        sum4 += 1
    elif p == 5:
        sum5 += 1
    elif p == 6:
        sum6 += 1

print(f'1的概率：{sum1/6000:.3f}')
print(f'2的概率：{sum2/6000:.3f}')
print(f'3的概率：{sum3/6000:.3f}')
print(f'4的概率：{sum4/6000:.3f}')
print(f'5的概率：{sum5/6000:.3f}')
print(f'6的概率：{sum6/6000:.3f}')