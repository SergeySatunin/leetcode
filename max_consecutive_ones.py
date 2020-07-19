# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:

        counter = 0
        max_counter = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                counter += 1
            else:
                max_counter = max(max_counter, counter)
                counter = 0

        return max(max_counter, counter)


nums = [0,0,1,1,0,1,1,1,1,1]

s = Solution()
result = s.findMaxConsecutiveOnes(nums)

print(result)