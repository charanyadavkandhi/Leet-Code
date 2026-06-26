from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        bit = [0] * (2 * n + 5)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        off = n + 2
        pre = ans = 0
        update(off)

        for x in nums:
            pre += 1 if x == target else -1
            ans += query(pre + off - 1)
            update(pre + off)

        return ans