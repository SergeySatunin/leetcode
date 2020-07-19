# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums, k: int):

        l = len(nums)

        if k % l == 0:
            return nums

        start_index = index = 0
        cur_el = nums[index]
        counter = 0

        while counter < l:
            new_position = (index + k) % l
            mem_el = nums[new_position]
            nums[new_position] = cur_el
            cur_el = mem_el

            if new_position == start_index:
                start_index += 1
                index = start_index
                cur_el = nums[index]
            else:
                index = new_position

            counter += 1

input = [1,2]
k = 2

s = Solution()
s.rotate(input, k)

print(input)
