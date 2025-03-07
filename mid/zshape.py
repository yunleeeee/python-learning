"""
很可惜，我的这个思路只解决了30%的样例，虽然认识到错误表明我在进步，但想了很久写了很久的
算法竟然是不完全正确，甚至完全不可行的，甚至被ai写的代码简洁性给秒杀，还是很让人沮丧的一件事
哎
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        current_row = 0
        direction = 1  # 控制移动方向，1表示向下，-1表示向上

        for char in s:
            rows[current_row] += char
            # 到达顶部或底部时改变方向
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            current_row += direction

        return ''.join(rows)
"""

s = input()
numsRows = int(input())
n = len(s)
cols = numsRows
rows = (n // (cols * 2 - 2)) * (cols - 1) + 1
zshape = []
for _ in range(rows):
    zshape.append([0] * cols)
t = 0  #记录位置，方便录入二维列表
for i in range(rows):
    for j in range(cols):
        if i == 0 or i % (cols-1) == 0:
            zshape[i][j] = s[t]
            if t == n-1:
                break
            t += 1
        elif j == cols - i % (cols-1) - 1:
            zshape[i][j] = s[t]
            if t == n-1:
                break
            t += 1
        else:
            zshape[i][j] = 0
result = []
for i in range(cols):
    for j in range(rows):
        if zshape[j][i] == 0:
            continue
        else:
            result.append(zshape[j][i])
print(''.join(result))


