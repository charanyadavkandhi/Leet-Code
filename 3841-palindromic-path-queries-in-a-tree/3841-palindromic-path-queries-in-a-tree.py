class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(200000)

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Euler tour and binary lifting for LCA
        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfs(u, p):
            nonlocal timer
            parent[0][u] = p
            tin[u] = timer
            timer += 1

            for v in adj[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)

            tout[u] = timer

        dfs(0, 0)

        for k in range(1, LOG):
            for u in range(n):
                parent[k][u] = parent[k - 1][parent[k - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        # Each node contributes its character bit to its subtree.
        # Fenwick tree stores XOR of character masks.
        bit = [0] * (n + 2)
        chars = [1 << (ord(c) - ord('a')) for c in s]

        def add(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def prefix(i):
            res = 0
            i += 1
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def subtree_xor(u):
            # XOR of characters in subtree u
            return prefix(tout[u] - 1) ^ (
                prefix(tin[u] - 1) if tin[u] > 0 else 0
            )

        # Use a difference Fenwick tree: updating a node toggles
        # its character throughout its subtree's root-path queries.
        for u in range(n):
            add(tin[u], chars[u])
            add(tout[u], chars[u]) if tout[u] < n else None

        def path_mask(u, v):
            w = lca(u, v)
            # Root-to-node masks are computed from the Euler
            # difference Fenwick tree.
            mu = prefix(tin[u])
            mv = prefix(tin[v])
            mw = prefix(tin[w])
            return mu ^ mv ^ chars[w]

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))

                if chars[u] != new_mask:
                    delta = chars[u] ^ new_mask
                    add(tin[u], delta)
                    if tout[u] < n:
                        add(tout[u], delta)
                    chars[u] = new_mask

            else:
                u, v = int(parts[1]), int(parts[2])
                mask = path_mask(u, v)
                ans.append((mask & (mask - 1)) == 0)

        return ans