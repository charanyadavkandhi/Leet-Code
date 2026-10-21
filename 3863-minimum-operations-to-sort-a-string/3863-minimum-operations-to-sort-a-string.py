class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        if n == 2:
            return -1
        mn, mx = min(s), max(s)
        # One op: sort everything except the first (or last) char
        if s[0] == mn or s[-1] == mx:
            return 1
        # Two ops: need s[-1] not strictly smaller than all others,
        # or s[0] not strictly larger than all others
        if s[-1] != mn or s.count(mn) > 1:
            return 2
        if s[0] != mx or s.count(mx) > 1:
            return 2
        return 3