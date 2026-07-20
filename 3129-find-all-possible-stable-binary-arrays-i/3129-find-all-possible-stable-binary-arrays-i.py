from functools import cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(z, o, last):
            if z == 0:
                return 1 if last == 1 and o <= limit else 0
            if o == 0:
                return 1 if last == 0 and z <= limit else 0

            if last == 0:
                ans = dp(z - 1, o, 0) + dp(z - 1, o, 1)
                if z > limit:
                    ans -= dp(z - limit - 1, o, 1)
            else:
                ans = dp(z, o - 1, 0) + dp(z, o - 1, 1)
                if o > limit:
                    ans -= dp(z, o - limit - 1, 0)

            return ans % MOD

        return (dp(zero, one, 0) + dp(zero, one, 1)) % MOD