# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        result = []
        prev_result = self.countAndSay(n-1)

        slow = 0
        fast = 0

        while fast < len(prev_result):
            while prev_result[slow] == prev_result[fast]:
                fast += 1
                if fast == len(prev_result):
                    break

            result.append(str(fast - slow))
            result.append(prev_result[slow])
            slow = fast

        return ''.join(result)


input = 10
s = Solution()
result = s.countAndSay(input)

print(result)