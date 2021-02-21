# https://leetcode.com/problems/subsets/

from typing import List
import copy

class Solution:
    def __init__(self):
      self.subs = []

    def helper(self, current_set, rest):
      self.subs.append(copy.deepcopy(current_set))
      for i, el in enumerate(rest):
        current_set.append(el)
        rest = [x for x in rest if x != el]
        self.helper(current_set, rest)
        current_set.remove(el)

    def subsets(self, nums: List[int]) -> List[List[int]]:
      self.helper([], nums)
      return self.subs



s = Solution()

print(s.subsets([1,2,3]))