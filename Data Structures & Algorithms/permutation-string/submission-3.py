from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = defaultdict(int)
        window_count = defaultdict(int)

        # Count frequencies of s1
        for c in s1:
            s1_count[c] += 1

        # Build the first window
        for i in range(len(s1)):
            window_count[s2[i]] += 1

        # Check the first window
        if s1_count == window_count:
            return True

        left = 0

        # Slide the window
        for right in range(len(s1), len(s2)):

            # Add new character
            window_count[s2[right]] += 1

            # Remove old character
            window_count[s2[left]] -= 1

            # Remove key if frequency becomes 0
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]

            left += 1

            if window_count == s1_count:
                return True

        return False