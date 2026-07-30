from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        start = 0
        length = 0
        for end in range(len(s)):
            while s[end] in c:
                c.remove(s[start])
                start += 1
            c.add(s[end])
            length = max(length, end - start + 1)
        return length

