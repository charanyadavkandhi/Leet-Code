from typing import List
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store: (left, right, weight, original_index)
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by left endpoint
        arr.sort()

        starts = [x[0] for x in arr]

        # next[i] = first interval whose left > arr[i].right
        nxt = [0] * n

        for i in range(n):
            r = arr[i][1]
            nxt[i] = bisect_right(starts, r)

        # dp(i, k) = (maximum score, lexicographically smallest indices)
        memo = {}

        def solve(i, k):
            if i >= n or k == 0:
                return (0, ())

            if (i, k) in memo:
                return memo[(i, k)]

            # Option 1: skip current interval
            score1, indices1 = solve(i + 1, k)

            # Option 2: take current interval
            score2, indices2 = solve(nxt[i], k - 1)

            current_index = arr[i][3]

            score2 += arr[i][2]
            indices2 = tuple(sorted((current_index,) + indices2))

            # Choose the better result
            if score2 > score1:
                ans = (score2, indices2)
            elif score2 < score1:
                ans = (score1, indices1)
            else:
                # Same score -> lexicographically smaller indices
                if indices2 < indices1:
                    ans = (score2, indices2)
                else:
                    ans = (score1, indices1)

            memo[(i, k)] = ans
            return ans

        return list(solve(0, 4)[1])