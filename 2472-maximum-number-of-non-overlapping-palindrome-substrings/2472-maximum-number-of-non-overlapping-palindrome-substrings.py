class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[l][r] = True if s[l:r+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r] and (length <= 2 or pal[l + 1][r - 1]):
                    pal[l][r] = True

        # dp[i] = max number of palindromes using s[0:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't select a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # Try every possible starting position
            for l in range(i - k + 1):
                if pal[l][i - 1]:
                    dp[i] = max(dp[i], dp[l] + 1)

        return dp[n]