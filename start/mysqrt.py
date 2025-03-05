#我的方法：暴力枚举，时间复杂度On
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        if x == 4:
            return 2

        for i in range(x // 2 + 1):
            if i * i == x:
                return i

            elif i * i <= x < (i + 1) * (i + 1):
                return i

#二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        l,r,ans = 0,x,-1
        while r >= l:
            mid = (l+r)//2
            if mid * mid <= x:
                ans = mid
                l = mid + 1  #必须更新为mid+1 否则可能无限循环导致超时
            else:
                r = mid - 1
        return ans



