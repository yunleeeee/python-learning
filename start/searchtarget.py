class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums[i+1:]:
                return [i,nums[i+1:].index(res) + i +1] #切片操作后，索引留在0，所以需要加i+1
