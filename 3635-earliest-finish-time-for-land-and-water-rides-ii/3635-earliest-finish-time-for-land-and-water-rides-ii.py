from bisect import bisect_right
from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def preprocess(start, duration):
            rides = sorted(zip(start, duration))
            s = [x for x, _ in rides]
            d = [y for _, y in rides]

            n = len(rides)

            pref = [0] * n
            pref[0] = d[0]
            for i in range(1, n):
                pref[i] = min(pref[i - 1], d[i])

            suff = [0] * n
            suff[-1] = s[-1] + d[-1]
            for i in range(n - 2, -1, -1):
                suff[i] = min(suff[i + 1], s[i] + d[i])

            return s, pref, suff

        def query(c, starts, pref, suff):
            idx = bisect_right(starts, c) - 1

            ans = float('inf')

            if idx >= 0:
                ans = min(ans, c + pref[idx])

            if idx + 1 < len(starts):
                ans = min(ans, suff[idx + 1])

            return ans

        waterStarts, waterPref, waterSuff = preprocess(
            waterStartTime, waterDuration
        )

        landStarts, landPref, landSuff = preprocess(
            landStartTime, landDuration
        )

        ans = float('inf')

        # Land -> Water
        for s, d in zip(landStartTime, landDuration):
            completion = s + d
            ans = min(
                ans,
                query(completion, waterStarts, waterPref, waterSuff)
            )

        # Water -> Land
        for s, d in zip(waterStartTime, waterDuration):
            completion = s + d
            ans = min(
                ans,
                query(completion, landStarts, landPref, landSuff)
            )

        return ans