from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = defaultdict(list)

        for w in strs:
            k ="".join(sorted(w))
            di[k].append(w)
        return list(di.values())
