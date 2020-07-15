# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums):

        min_int = -9223372036854775807
        first_max = nums[0]
        second_max = min_int
        third_max = min_int

        for el in nums:
            if el > first_max:
                third_max = second_max
                second_max = first_max
                first_max = el

            elif el > second_max and el < first_max:
                third_max = second_max
                second_max = el

            elif el > third_max and el < second_max:
                third_max = el

        return third_max if third_max > min_int else first_max
    

nums = [2, 2, 3, 1]
s = Solution()
result = s.thirdMax(nums)

print(result)



