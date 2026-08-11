class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0
            if i + 2 * M >= n:
                return suffix[i]
            best = 0
            for X in range(1, 2 * M + 1):
                opponent = dp(i + X, max(M, X))
                current = suffix[i] - opponent
                best = max(best, current)
            return best
        return dp(0, 1)