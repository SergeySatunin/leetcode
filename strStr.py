# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str):

        if haystack == needle:
            return 0

        if needle == '':
            return 0

        for i, el in enumerate(haystack):
            if el == needle[0] and len(needle) <= len(haystack) - i:
                check_result = True
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        check_result = False
                        break
                if check_result:
                    return i
        return -1



s  = Solution()
result = s.strStr("mississippi", "issipi")

print(result)