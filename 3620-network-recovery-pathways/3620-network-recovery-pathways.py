from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        g = [[] for _ in range(n)]
        indeg = [0] * n
        w = []

        for u, v, c in edges:
            g[u].append((v, c))
            indeg[v] += 1
            w.append(c)

        # Topological order
        q = deque(i for i in range(n) if indeg[i] == 0)
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        if not w:
            return -1

        vals = sorted(set(w))

        def check(x):
            INF = 10**18
            dp = [INF] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == INF:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, c in g[u]:
                    if c < x:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    dp[v] = min(dp[v], dp[u] + c)
            return dp[n - 1] <= k

        if not check(vals[0]):
            return -1

        l, r = 0, len(vals) - 1
        ans = vals[0]
        while l <= r:
            mid = (l + r) // 2
            if check(vals[mid]):
                ans = vals[mid]
                l = mid + 1
            else:
                r = mid - 1
        return ans