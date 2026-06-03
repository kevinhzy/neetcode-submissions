class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            x = tuple(sorted(Counter(s).items()))
            seen[x].append(s)
        return list(seen.values())