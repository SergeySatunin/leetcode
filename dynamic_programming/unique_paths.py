# https://leetcode.com/problems/unique-paths/

class Solution:
    def __init__(self):
        self.cache = {}
        self.cache['1_1'] = 1

    def uniquePaths(self, m: int, n: int) -> int:
        k = str(m)+'_'+str(n)

        if k in self.cache:
            return self.cache[k]

        from_top = 0 if m - 1 < 0 else self.uniquePaths(m - 1, n)
        from_left = 0 if n - 1 < 0 else self.uniquePaths(m, n - 1)
        result = from_top + from_left

        self.cache[k] = result

        return self.cache[k]




s = Solution()
result = s.uniquePaths(3,3)

print(result)