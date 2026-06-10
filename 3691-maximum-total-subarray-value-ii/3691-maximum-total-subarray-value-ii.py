from heapq import *

class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        m = lg[n] + 1
        mx = [[0] * m for _ in range(n)]
        mn = [[0] * m for _ in range(n)]

        for i, x in enumerate(nums):
            mx[i][0] = mn[i][0] = x

        for j in range(1, m):
            d = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                mx[i][j] = max(mx[i][j - 1], mx[i + d][j - 1])
                mn[i][j] = min(mn[i][j - 1], mn[i + d][j - 1])

        def val(l, r):
            j = lg[r - l + 1]
            return max(mx[l][j], mx[r - (1 << j) + 1][j]) - \
                   min(mn[l][j], mn[r - (1 << j) + 1][j])

        pq = [(-val(i, n - 1), i, n - 1) for i in range(n)]
        heapify(pq)

        ans = 0
        for _ in range(k):
            v, l, r = heappop(pq)
            ans -= v
            if l < r:
                heappush(pq, (-val(l, r - 1), l, r - 1))

        return ans