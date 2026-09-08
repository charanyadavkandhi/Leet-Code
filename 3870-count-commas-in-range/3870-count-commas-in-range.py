class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0

        for i in range(1000, n + 1):
            ans += (len(str(i)) - 1) // 3

        return ans