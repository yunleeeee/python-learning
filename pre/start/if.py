height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2

print(f'BMI:{bmi:.1f}')
print('BMI:%.1f' % bmi)

if 18.5 <= bmi <= 24:
    print('你的身材真的很棒')
elif bmi <= 18.5:
    print('你有点瘦了')
else:
    print('你有点胖了')
