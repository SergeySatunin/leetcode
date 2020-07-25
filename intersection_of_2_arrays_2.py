from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        c1 = Counter(nums1)
        result = []

        for i in nums2:
            if i in c1 and c1[i] > 0:
                result.append(i)
                c1[i] -= 1

        return result
    

nums1 = [1,2,2,1]
nums2 = [2,2]
s = Solution()
result = s.intersect(nums1, nums2)

print(result)