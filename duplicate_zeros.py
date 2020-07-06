# https://leetcode.com/articles/duplicate-zeros/

class BrutforceSolution:
    def duplicateZeros(self, arr) -> None:

        i = 0
        while i < len(arr):
            if arr[i] == 0:
                for j in range(len(arr) - 1, i + 1, -1):
                    arr[j] = arr[j-1]
                if i+1 < len(arr):
                    arr[i+1] = 0
                i += 2
            else:
                i += 1

class Solution:
    def duplicateZeros(self, arr) -> None:

        possible_dups = 0
        is_edge_case = 0

        l = len(arr) - 1

        for i in range(l + 1):

            if arr[i] == 0:
                #Edge case - a zero that can't be duplicated, but needs to be copied once
                if i + possible_dups == l:
                    arr[l] = 0
                    is_edge_case = 1
                    break

                if i + possible_dups > l:
                    break

                possible_dups += 1

        for i in range(l - possible_dups - is_edge_case, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                arr[i + possible_dups - 1] = 0
                possible_dups -= 1
            else:
                arr[i + possible_dups] = arr[i]


s = Solution()

l = [8,4,5,0,0,0,0,7]
s.duplicateZeros(l)
print(l)


l = [0,1,2,3,4,5]
s.duplicateZeros(l)
print(l)

l = [0,1,2,0,4,5]
s.duplicateZeros(l)
print(l)

l = [0,0,0]
s.duplicateZeros(l)
print(l)