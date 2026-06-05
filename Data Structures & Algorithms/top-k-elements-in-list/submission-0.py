class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in counter.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(nums)):
            for num in freq[len(nums)-i]:
                res.append(num)
                if len(res) == k:
                    return res