# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits):

        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0

        if sum(digits) == 0:
            digits.insert(0, 1)

        return digits
    

nums = [9]

s = Solution()
result = s.plusOne(nums)

print(result)