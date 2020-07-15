# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# This solution uses a trick described in the video below (treating elements as indexes in the sorted array)
# https://www.youtube.com/watch?v=CTBEcmzLAuA

# Solution with set is straightforward, but requires extra memory

class Solution:
    def findDisappearedNumbers(self, nums):

        result = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -1 * abs(nums[index])

        for i, el in enumerate(nums):
            if el > 0:
                result.append(i + 1)

        return result


class SetSolution:
    def findDisappearedNumbers(self, nums):
        nums_set = set(nums)
        return [x for x in range(1, len(nums) + 1) if x not in nums_set]



nums = [4,3,2,7,8,2,3,1]

s = SetSolution()
result = s.findDisappearedNumbers(nums)

print(result)