# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1

input = "ll"
s = Solution()
result = s.firstUniqChar(input)

print(result)