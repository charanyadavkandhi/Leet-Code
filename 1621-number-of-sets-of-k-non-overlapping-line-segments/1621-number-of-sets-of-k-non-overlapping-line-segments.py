class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        N = n + k - 1
        R = 2 * k

        dp = [0] * (R + 1)
        dp[0] = 1

        for i in range(1, N + 1):
            for j in range(min(i, R), 0, -1):
                dp[j] = (dp[j] + dp[j - 1]) % MOD

        return dp[R]