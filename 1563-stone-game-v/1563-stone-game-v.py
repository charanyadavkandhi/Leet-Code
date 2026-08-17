from bisect import bisect_right

class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[l][r] = maximum score for subarray l...r
        dp = [[0] * n for _ in range(n)]

        # leftBest[l][k] =
        # max(prefix[t+1] + dp[l][t]) for l <= t <= k
        leftBest = [[0] * n for _ in range(n)]

        # rightBest[k][r] =
        # max(dp[t][r] - prefix[t]) for k <= t <= r
        rightBest = [[0] * n for _ in range(n)]

        # Base cases: one stone
        for i in range(n):
            leftBest[i][i] = prefix[i + 1]
            rightBest[i][i] = -prefix[i]

        # Process intervals by increasing length
        for length in range(2, n + 1):

            for l in range(n - length + 1):
                r = l + length - 1

                total = prefix[r + 1] - prefix[l]

                # Find largest p such that:
                #
                # prefix[p] - prefix[l] <= total / 2
                #
                # p represents the prefix position.
                target = (2 * prefix[l] + total) // 2

                p = bisect_right(
                    prefix,
                    target,
                    l + 1,
                    r + 1
                ) - 1

                best = 0

                # Case 1:
                # left <= right
                #
                # Split k is from l to p-1.
                if p >= l + 1:
                    best = max(
                        best,
                        leftBest[l][p - 1] - prefix[l]
                    )

                # Case 2:
                # right <= left
                #
                # If the sums are exactly equal at p,
                # the right part starts at p.
                #
                # Otherwise it starts at p+1.
                if (
                    p >= l + 1
                    and 2 * (prefix[p] - prefix[l]) == total
                ):
                    start = p
                else:
                    start = p + 1

                if start <= r:
                    best = max(
                        best,
                        prefix[r + 1] + rightBest[start][r]
                    )

                dp[l][r] = best

                # Update left auxiliary table
                leftBest[l][r] = max(
                    leftBest[l][r - 1],
                    prefix[r + 1] + dp[l][r]
                )

                # Update right auxiliary table
                rightBest[l][r] = max(
                    rightBest[l + 1][r],
                    dp[l][r] - prefix[l]
                )

        return dp[0][n - 1]