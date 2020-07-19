# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers, target: int):

        size = len(numbers)

        if size < 2:
            return  []

        l = 0
        r = size - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1 , r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

        return []


numbers = [0]
target = -2

s = Solution()
result = s.twoSum(numbers, target)

print(result)