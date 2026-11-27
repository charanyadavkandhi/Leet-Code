
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        # Step 1: Calculate free copies for every item
        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        # Step 2: Group items by price
        groups = {}

        for i, (factor, price) in enumerate(items):
            groups.setdefault(price, []).append(1 + free[i])

        # dp[c] = maximum value using items with higher prices
        # and spending exactly c
        dp = [-1] * (budget + 1)
        dp[0] = 0

        ans = 0

        # Process prices in descending order
        for p in sorted(groups.keys(), reverse=True):

            # Snapshot: items with price strictly greater than p
            base = dp[:]

            # dp_has[c] = maximum value spending c,
            # selecting at least one item costing p
            dp_has = [-1] * (budget + 1)

            for value in groups[p]:

                for c in range(budget, p - 1, -1):

                    # Select the first item of price p
                    if base[c - p] != -1:
                        dp_has[c] = max(
                            dp_has[c],
                            base[c - p] + value
                        )

                    # Select another item of price p
                    if dp_has[c - p] != -1:
                        dp_has[c] = max(
                            dp_has[c],
                            dp_has[c - p] + value
                        )

            # Calculate answer using additional purchases
            for c in range(p, budget + 1):
                if dp_has[c] != -1:
                    extra = (budget - c) // p
                    ans = max(ans, dp_has[c] + extra)

            # Update ordinary knapsack for the next price group
            for value in groups[p]:
                for c in range(budget, p - 1, -1):
                    if dp[c - p] != -1:
                        dp[c] = max(dp[c], dp[c - p] + value)

        return ans
