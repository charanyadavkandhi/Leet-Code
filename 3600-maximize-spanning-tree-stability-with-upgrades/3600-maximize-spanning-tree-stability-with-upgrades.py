class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        if self.rank[x] < self.rank[y]:
            x, y = y, x

        self.parent[y] = x

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

        return True


class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:

        def check(limit):
            dsu = DSU(n)
            used = 0
            cnt = 0

            # Mandatory edges
            for u, v, s, must in edges:
                if must:
                    if s < limit:
                        return False

                    if not dsu.union(u, v):
                        return False

                    cnt += 1

            # Optional edges without upgrade
            for u, v, s, must in edges:
                if must:
                    continue

                if s >= limit:
                    if dsu.union(u, v):
                        cnt += 1

            # Optional edges with upgrade
            for u, v, s, must in edges:
                if must:
                    continue

                if s < limit and s * 2 >= limit:
                    if dsu.union(u, v):
                        cnt += 1
                        used += 1

            return cnt == n - 1 and used <= k

        hi = 0
        for _, _, s, _ in edges:
            hi = max(hi, 2 * s)

        lo = 0
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans