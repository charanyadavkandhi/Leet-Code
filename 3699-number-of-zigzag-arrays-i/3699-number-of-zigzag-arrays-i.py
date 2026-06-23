class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        up = [i for i in range(m)]
        down = [m - 1 - i for i in range(m)]

        for _ in range(3, n + 1):
            pu = [0]
            pd = [0]

            for x in up:
                pu.append((pu[-1] + x) % MOD)
            for x in down:
                pd.append((pd[-1] + x) % MOD)

            up = [pd[i] for i in range(m)]
            down = [(pu[m] - pu[i + 1]) % MOD for i in range(m)]

        return (sum(up) + sum(down)) % MOD