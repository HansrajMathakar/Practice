class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        lsum = 0
        rsum = sum(nums[1:])
        
        if lsum == rsum:
            return 0
        
        for i in range(1, len(nums)):
            lsum += nums[i-1]
            rsum -= nums[i]
            if lsum == rsum:
                return i
        
        return -1
