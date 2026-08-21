from math import gcd
from functools import reduce

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:

        # Remove coins that are multiples of another smaller coin.
        # They don't add any new amounts.
        coins.sort()
        filtered = []

        for c in coins:
            if not any(c % x == 0 for x in filtered):
                filtered.append(c)

        coins = filtered
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            """Number of distinct valid amounts <= x."""
            total = 0

            # Inclusion-exclusion over all subsets
            for mask in range(1, 1 << n):
                L = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        L = lcm(L, coins[i])

                        # L is already larger than x
                        if L > x:
                            valid = False
                            break

                if not valid:
                    continue

                ways = x // L

                if bits % 2 == 1:
                    total += ways
                else:
                    total -= ways

            return total

        # Binary search for the smallest x
        # such that at least k valid amounts <= x.
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left