# https://leetcode.com/problems/next-permutation/
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        r = len(nums) - 1

        while r - 1 >= 0 and nums[r-1] >= nums[r]:
            r -= 1

        if r == 0:
            nums.reverse()
            return nums

        pivot = r - 1
        tail = len(nums) - 1
        while nums[tail] <= nums[pivot]:
            tail -= 1

        nums[pivot], nums[tail] = nums[tail], nums[pivot]

        l = pivot + 1
        r = len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums

s = Solution()

#[1,5,8,4,7,6,5,3,1]
result = s.nextPermutation([1,5,8,4,7,6,5,3,1])

print(result)