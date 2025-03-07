"""def lcm(x:int,y:int) -> int:
    if x < y:
        x,y = y,x
    for i in range(1,y+1):
        if x * i % y == 0:
            return x * i
m = int(input())
n = int(input())
print(lcm(m,n))"""
def lcm(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    for i in range(1, y + 1):
        if x * i % y == 0:
            return x * i

m = int(input("请输入第一个整数: "))
n = int(input("请输入第二个整数: "))
print(f"{m} 和 {n} 的最小公倍数是: {lcm(m, n)}")

def gcd(x: int, y: int) -> int:
    """求最大公约数"""
    while y % x != 0:
        x, y = y % x, x
    return x