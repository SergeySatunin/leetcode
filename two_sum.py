# https://leetcode.com/problems/two-sum/

from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = defaultdict(int)
        for i, el in enumerate(nums):
            if (target - el) in hm.keys():
                return [hm[target - el], i]
            else:
                hm[el] = i

nums = [2, 7, 11, 15]
target = 9

s = Solution()
result = s.twoSum(nums, target)
print(result)