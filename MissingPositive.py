class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        for i in range(1, len(nums)+2):
            if i not in nums:
                return i
