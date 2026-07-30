from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        start = 0
        length = 0 
        for end in range(len(s)):
            d[s[end]] += 1
            mostfreq = max(d.values())
            tlength = end - start + 1
            repreq = tlength - mostfreq
            while repreq > k:
                d[s[start]] -= 1
                start += 1
                tlength = end - start + 1
                repreq = tlength - mostfreq
            length = max(tlength,length)
        return length