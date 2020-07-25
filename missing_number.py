# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

s = Solution()
result = s.missingNumber([9,6,4,2,3,5,7,0,1])

print(result)