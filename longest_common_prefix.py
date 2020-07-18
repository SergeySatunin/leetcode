# https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        first = strs[0]
        result = []

        for i, el in enumerate(first):
            check_status = True

            for word in strs[1::]:
                if i == len(word) or word[i] != el:
                    check_status = False
                    break

            if check_status:
                result.append(el)
            else:
                break

        return "" if len(result) == 0 else ''.join(result)



strs = []
s = Solution()
result = s.longestCommonPrefix(strs)

print(result)
print()