class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 初始化两个指针
        slow = 0

        for fast in range(1, nums.length):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        # 返回新数组的长度
        return slow + 1

#对于需要缩短列表长度的题目，我们可以使用双指针
#使得慢速的指针指向正确的元素，而快速的指针用于遍历寻找正确元素