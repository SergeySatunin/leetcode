import math

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        symbols = []

        symbol = x % 10
        x //= 10

        while x > 0 or (x == 0 and symbol > 0):
            symbols.append(symbol)
            symbol = x % 10
            x //= 10

        result = 0
        for i in range(len(symbols)):
            result += math.pow(10, len(symbols) - 1 - i) * symbols[i]

        return int(result * sign)

s = Solution()
result = s.reverse(0)

print(result)