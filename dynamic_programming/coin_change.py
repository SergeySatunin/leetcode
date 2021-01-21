from typing import List
import functools

class Solution:

    def __init__(self):
        self.options = []
        pass

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        @functools.lru_cache(None)
        def try_coin(amt, cnt):
            for c in coins:
                if amt == c:
                    self.options.append(cnt + 1)
                    return 1
                if amt - c < 0:
                    return -1
                else:
                    try_coin(amt - c, cnt + 1)

        try_coin(amount, 0)
        return min(self.options) if len(self.options) > 0 else -1


s = Solution()

result = s.coinChange([2], 3)

print(result)