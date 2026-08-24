class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Prefix sum
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # If Alice takes all stones
        best = prefix[n - 1]

        # Try every possible prefix of length >= 2
        for i in range(n - 2, 0, -1):
            best = max(best, prefix[i] - best)

        return best