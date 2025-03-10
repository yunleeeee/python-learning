class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        if not self.is_valid(a, b, c):
            raise ValueError("无法构成三角形")
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


# 测试代码
try:
    t = Triangle(3, 4, 5)
    print(f'周长: {t.perimeter}')
    print(f'面积: {t.area}')
except ValueError as e:
    print(e)

try:
    t = Triangle(1, 2, 3)  # 这个无法构成三角形
    print(f'周长: {t.perimeter}')
    print(f'面积: {t.area}')
except ValueError as e:
    print(e)