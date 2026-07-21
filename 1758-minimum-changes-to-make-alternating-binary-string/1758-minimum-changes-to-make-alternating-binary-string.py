class Solution:
    def minOperations(self, s: str) -> int:
        start0 = 0
        start1 = 0

        for i, ch in enumerate(s):
            if ch != ("0" if i % 2 == 0 else "1"):
                start0 += 1
            if ch != ("1" if i % 2 == 0 else "0"):
                start1 += 1

        return min(start0, start1)