class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        px = [[0] * (n + 1) for _ in range(m + 1)]
        py = [[0] * (n + 1) for _ in range(m + 1)]

        ans = 0

        for i in range(m):
            for j in range(n):
                px[i + 1][j + 1] = px[i][j + 1] + px[i + 1][j] - px[i][j]
                py[i + 1][j + 1] = py[i][j + 1] + py[i + 1][j] - py[i][j]

                if grid[i][j] == 'X':
                    px[i + 1][j + 1] += 1
                elif grid[i][j] == 'Y':
                    py[i + 1][j + 1] += 1

                if px[i + 1][j + 1] == py[i + 1][j + 1] and px[i + 1][j + 1] > 0:
                    ans += 1

        return ans