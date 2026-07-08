class Solution:
    def maxProductPath(self, grid):
        m, n = len(grid), len(grid[0])
        mx = [[0] * n for _ in range(m)]
        mn = [[0] * n for _ in range(m)]
        mx[0][0] = mn[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                a = []
                if i:
                    a += [mx[i - 1][j], mn[i - 1][j]]
                if j:
                    a += [mx[i][j - 1], mn[i][j - 1]]
                mx[i][j] = max(x * grid[i][j] for x in a)
                mn[i][j] = min(x * grid[i][j] for x in a)

        return -1 if mx[-1][-1] < 0 else mx[-1][-1] % (10**9 + 7)