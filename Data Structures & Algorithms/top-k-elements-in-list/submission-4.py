from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        l = []
        for i in nums:
            h[i] = h.get(i, 0) + 1
        
        l = sorted(h, key = h.get, reverse = True)

        return l[:k]
        