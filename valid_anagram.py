# https://leetcode.com/problems/valid-anagram/

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


input1 = "anagram"
input2 = "nagaram"

s = Solution()
result = s.isAnagram(input1, input2)

print(result)