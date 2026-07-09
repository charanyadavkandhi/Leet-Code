class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        ans = set()

        for i in range(m):
            for j in range(n):
                ans.add(grid[i][j])
                d = 1
                while i - d >= 0 and i + d < m and j - d >= 0 and j + d < n:
                    s = 0
                    x, y = i - d, j
                    for k in range(d):
                        s += grid[x + k][y + k]
                    x, y = i, j + d
                    for k in range(d):
                        s += grid[x + k][y - k]
                    x, y = i + d, j
                    for k in range(d):
                        s += grid[x - k][y - k]
                    x, y = i, j - d
                    for k in range(d):
                        s += grid[x - k][y + k]
                    ans.add(s)
                    d += 1

        return sorted(ans, reverse=True)[:3]