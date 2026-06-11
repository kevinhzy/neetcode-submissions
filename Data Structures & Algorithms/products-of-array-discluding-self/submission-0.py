class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suff = [1] * len(nums),[1] * len(nums)
        res = []
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        for i in range(len(nums)):
            res.append(pre[i] * suff[i])
        return res