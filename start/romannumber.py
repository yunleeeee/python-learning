class Solution(object):
    def romanToInt(self, s):
        nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # 特殊情况，用于处理减法规则
        subtractive = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        total = 0
        # 处理减法规则的特殊情况
        for symbol, value in subtractive.items():
            if symbol in s:
                total += value  # 加上特殊情况的值
                s = s.replace(symbol, "", 1)  # 移除特殊情况的符号
        # 处理剩下的普通情况
        for i in s:
            total += nums[i]

        return total
