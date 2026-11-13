from typing import List
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        right = n - 1
        cost = 0
        ans = 0

        for left in range(n - 1, -1, -1):
            x = nums[left]
            cnt = 1
            total = x

            while dq and dq[0][0] <= x:
                v, c, s = dq.popleft()
                cost -= v * c - s
                cnt += c
                total += s

            dq.appendleft([x, cnt, total])
            cost += x * cnt - total

            while cost > k:
                v, c, s = dq[-1]
                y = nums[right]
                cost -= v - y

                dq[-1][1] -= 1
                dq[-1][2] -= y

                if dq[-1][1] == 0:
                    dq.pop()

                right -= 1

            ans += right - left + 1

        return ans