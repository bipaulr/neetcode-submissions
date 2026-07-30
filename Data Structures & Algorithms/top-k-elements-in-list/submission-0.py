from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n]+=1
        freq = sorted(d.items(), key = lambda x:x[1], reverse = True)
        return [freq[i][0] for i in range(k)]