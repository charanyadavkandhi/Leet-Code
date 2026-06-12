class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = n.bit_length()
        par = [[0] * (n + 1) for _ in range(LOG)]
        dep = [0] * (n + 1)

        st = [(1, 0)]
        while st:
            u, p = st.pop()
            par[0][u] = p
            for v in g[u]:
                if v != p:
                    dep[v] = dep[u] + 1
                    st.append((v, u))

        for k in range(1, LOG):
            for v in range(1, n + 1):
                par[k][v] = par[k - 1][par[k - 1][v]]

        def lca(a, b):
            if dep[a] < dep[b]:
                a, b = b, a

            d = dep[a] - dep[b]
            for k in range(LOG):
                if d >> k & 1:
                    a = par[k][a]

            if a == b:
                return a

            for k in range(LOG - 1, -1, -1):
                if par[k][a] != par[k][b]:
                    a, b = par[k][a], par[k][b]

            return par[0][a]

        ans = []
        for u, v in queries:
            d = dep[u] + dep[v] - 2 * dep[lca(u, v)]
            ans.append(0 if d == 0 else pow(2, d - 1, MOD))
        return ans