from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]

            res = float("inf")
            for c in coins:
                if remaining >= c:
                    res = min(res, 1 + dfs(remaining - c))

            memo[remaining] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins == float("inf") else minCoins