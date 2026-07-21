class Solution:
    def minSwaps(self, grid):
        n = len(grid)

        zeros = []
        for row in grid:
            cnt = 0
            for x in row[::-1]:
                if x == 0:
                    cnt += 1
                else:
                    break
            zeros.append(cnt)

        ans = 0

        for i in range(n):
            need = n - i - 1
            j = i

            while j < n and zeros[j] < need:
                j += 1

            if j == n:
                return -1

            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                ans += 1
                j -= 1

        return ans