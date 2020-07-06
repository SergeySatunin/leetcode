#https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:

        if n == 0:
            return nums1

        p1 = m - 1
        p2 = n - 1

        i = 0
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[m + n - i - 1] = nums1[p1]
                p1 -= 1
            else:
                nums1[m + n - i - 1] = nums2[p2]
                p2 -= 1
            i += 1

        if p2 >= 0:
            for i in range(p2 + 1):
                nums1[i] = nums2[i]


arr1 = [2,0]
m = 1

arr2 = [1]
n = 1

s = Solution()
s.merge(arr1, m, arr2, n)

print(arr1)