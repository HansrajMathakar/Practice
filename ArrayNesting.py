class Solution:
    def arrayNesting(self, nums: 'List[int]') -> 'int':
        res = 0
        n = len(nums)
        for i in range(n):
            if nums[i] >= 0:
                j = i
                tmp = 0
                while nums[j] >= 0:
                    tmp += 1
                    nums[j] -= n
                    j = nums[j] + n
                res = max(res,tmp)
        return res
