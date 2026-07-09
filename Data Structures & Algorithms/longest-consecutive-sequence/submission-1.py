class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        longest = 1
        for num in nums:
            if num-1 in numSet:
                continue
            l = 1
            while num+l in numSet:
                l += 1
            if l > longest:
                longest = l
        return longest