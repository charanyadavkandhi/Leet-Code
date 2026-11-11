
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        both = min(need1, need2)

        # Buy individual items
        ans1 = need1 * cost1 + need2 * cost2

        # Buy type 3 items for the common requirement
        ans2 = both * costBoth + (need1 - both) * cost1 + (need2 - both) * cost2

        # Buy only type 3 items
        ans3 = max(need1, need2) * costBoth

        return min(ans1, ans2, ans3)
