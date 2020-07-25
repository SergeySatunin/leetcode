# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()

        l = 0
        r = len(s) - 1
        result = True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -=1
            else:
                result = False
                break

        return result

s = Solution()
result = s.isPalindrome("race a car")

print(result)