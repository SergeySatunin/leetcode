from collections import Counter
from typing import List

class Solution:

    def __init__(self):
        self.color_counter = Counter()

    def sortColors(self, nums: List[int]) -> None:
        for i, el in enumerate(nums):
            self.color_counter[el] += 1

        l = r = 0
        
        for color in [0, 1, 2]:
            r = l + self.color_counter[color]
            
            for i in range(l, r):
                nums[i] = color
            
            l = r
        
        return nums


s = Solution()
print(s.sortColors([1,1,1,1,1]))

