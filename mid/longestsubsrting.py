def lengthofsubstring(s:str) -> int:
    charset = set()  #使用滑动数组
    left = 0
    maxlength = 0

    for right in range(len(s)):
        while s[right] in charset:
            charset.remove(s[left])
            left += 1
        charset.add(s[right])
        maxlength = max(maxlength,right-left+1)

    return maxlength
