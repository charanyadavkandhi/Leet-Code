class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        i, j = x, x + k - 1
        while i < j:
            for c in range(y, y + k):
                grid[i][c], grid[j][c] = grid[j][c], grid[i][c]
            i += 1
            j -= 1
        return grid