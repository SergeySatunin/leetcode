from typing import List
class Solution:
    def __init__(self):
        self.input_size = 0
        self.result = []

    def helper(self, nums, solution):
        if len(solution) == self.input_size:
            self.result.append(solution.copy())
            return

        for i, n in enumerate(nums):
            solution.append(nums[i])
            self.helper(nums[:i] + nums[i+1:], solution)
            solution.pop()


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.input_size = len(nums)
        self.helper(nums, [])

        return self.result


s = Solution()
print(s.permute([1,2,3,4,5,6]))
