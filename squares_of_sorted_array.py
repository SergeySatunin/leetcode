# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums):

        l = len(nums)
        if l == 0:
            return nums

        result = []

        i = 0
        while i < l and nums[i] < 0:
            i += 1

        pos = i
        neg = i - 1

        while neg >= 0 and pos < l:
            if abs(nums[pos]) < abs(nums[neg]):
                result.append(nums[pos]**2)
                pos += 1
            else:
                result.append(nums[neg]**2)
                neg -= 1

        if neg >= 0:
            result.extend([x**2 for x in nums[neg::-1]])

        if pos < l:
            result.extend([x**2 for x in nums[pos:l]])

        return result

#nums = [-4,-1,0,3,10]
nums = [-1,-1,-1,1,1,1]

s = Solution()
result = s.sortedSquares(nums)

print(result)