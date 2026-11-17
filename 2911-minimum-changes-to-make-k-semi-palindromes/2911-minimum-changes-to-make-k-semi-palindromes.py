
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        # Precompute minimum changes for every substring
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                best = float('inf')

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for r in range(d):
                        left = i + r
                        right = i + r + ((length - 1 - r) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        # DP: partition into exactly k substrings
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for t in range(1, k + 1):
            for i in range(2 * t, n + 1):
                for j in range(2 * (t - 1), i - 1):
                    dp[t][i] = min(
                        dp[t][i],
                        dp[t - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
