class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        last = {}
        new_parent = parent[:]

        def dfs(node):
            ch = s[node]
            old = last.get(ch)

            if old is not None:
                new_parent[node] = old

            last[ch] = node

            for child in children[node]:
                dfs(child)

            if old is None:
                last.pop(ch, None)
            else:
                last[ch] = old

        dfs(0)

        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[new_parent[i]].append(i)

        ans = [1] * n

        def calc(node):
            for child in tree[node]:
                ans[node] += calc(child)
            return ans[node]

        calc(0)
        return ans