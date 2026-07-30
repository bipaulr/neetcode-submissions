from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        d = defaultdict(int)
        for i in range(len(s1)):
            d[s1[i]]+=1
        start = 0
        end = start + len(s1)
        dt = defaultdict(int)
        while end <= len(s2):
            for i in range(start,end):
                dt[s2[i]] +=1
            if dt == d:
                return True
            dt.clear()
            start+=1
            end = start + len(s1)
        return False
            
                



        