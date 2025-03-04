from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # 找到最短字符串的长度
        min_length = min(len(s) for s in strs)

        if min_length == 0:
            return ""

        # 初始化前缀为第一个字符串
        prefix = strs[0][:min_length]

        for i in range(min_length):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return prefix[:i] #prefix[:0] = ''空字符

        return prefix