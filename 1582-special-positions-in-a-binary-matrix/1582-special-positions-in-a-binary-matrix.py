class Solution:
    def numSpecial(self, mat):
        rows = [sum(r) for r in mat]
        cols = [sum(c) for c in zip(*mat)]

        ans = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    ans += 1

        return ans