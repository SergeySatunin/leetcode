# https://leetcode.com/articles/move-zeroes/

class Solution:
    def moveZeroes(self, nums) -> None:

        read_pointer = 0
        write_pointer = 0

        while read_pointer < len(nums):

            if nums[read_pointer] == 0:
                read_pointer += 1
                continue

            nums[write_pointer] = nums[read_pointer]

            write_pointer += 1
            read_pointer += 1

        while write_pointer < len(nums):
            nums[write_pointer] = 0
            write_pointer += 1


nums = [1,3,12]
s = Solution()
s.moveZeroes(nums)
print(nums)

print()