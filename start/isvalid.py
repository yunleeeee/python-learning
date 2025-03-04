class Solution:
    def isValid(self, s: str) -> bool:
        m = []
        if not s:
            return True
        for char in s:
            if char in '({[': #关键改变，与c有较大差别
                m.append(char)  #对于空列表需要用append添加元素
            else:
                if not m:
                    return False
                top = m.pop()  #top存储顶端元素
                if char == ')' and top != '(':
                    return False

                elif char == '}' and top != '{':
                    return False
                elif char == ']' and top != '[':
                    return False
        return not m

    """
    取代   elif s[i] == '}':
                if m[t] == '{':
                    m.pop()
                    t -= 1
                else: return False
    """