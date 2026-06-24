class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        if n == 1:
            return m

        sz = 2 * m

        T = [[0] * sz for _ in range(sz)]

        for x in range(m):
            for y in range(x):
                T[x][m + y] = 1

            for y in range(x + 1, m):
                T[m + x][y] = 1

        def matmul(A, B):
            n1 = len(A)
            n2 = len(B[0])
            k = len(B)

            C = [[0] * n2 for _ in range(n1)]

            for i in range(n1):
                for t in range(k):
                    if A[i][t]:
                        a = A[i][t]
                        for j in range(n2):
                            C[i][j] = (C[i][j] + a * B[t][j]) % MOD

            return C

        def matpow(M, p):
            n = len(M)

            R = [[0] * n for _ in range(n)]
            for i in range(n):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = matmul(R, M)

                M = matmul(M, M)
                p >>= 1

            return R

        base = [[0] for _ in range(sz)]

        for x in range(m):
            base[x][0] = x
            base[m + x][0] = m - 1 - x

        if n == 2:
            return sum(row[0] for row in base) % MOD

        P = matpow(T, n - 2)

        res = matmul(P, base)

        ans = 0
        for i in range(sz):
            ans = (ans + res[i][0]) % MOD

        return ans