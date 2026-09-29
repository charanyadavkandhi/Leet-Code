class Solution:

    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # Path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):

                change = 1 if grid[i][j] == '(' else -1

                # Starting cell
                if i == 0 and j == 0:
                    if change < 0:
                        return False

                    dp[j].add(change)
                    continue

                current = set()

                # From top
                if i > 0:
                    for balance in dp[j]:
                        new_balance = balance + change

                        if new_balance >= 0:
                            current.add(new_balance)

                # From left
                if j > 0:
                    for balance in dp[j - 1]:
                        new_balance = balance + change

                        if new_balance >= 0:
                            current.add(new_balance)

                dp[j] = current

        return 0 in dp[n - 1]