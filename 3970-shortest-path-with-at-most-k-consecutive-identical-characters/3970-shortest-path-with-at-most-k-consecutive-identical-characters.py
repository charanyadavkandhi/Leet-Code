
from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        if k == 0:
            return -1

        pq = [(0, 0, 1)]
        dist = {}

        while pq:
            cost, node, count = heapq.heappop(pq)

            if (node, count) in dist:
                continue

            dist[(node, count)] = cost

            if node == n - 1:
                return cost

            for nei, weight in adj[node]:
                if labels[nei] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count <= k and (nei, new_count) not in dist:
                    heapq.heappush(
                        pq,
                        (cost + weight, nei, new_count)
                    )

        return -1
