from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            x = num % k

            # New subarrays ending at current position
            new_dp = [0] * k

            # Start a new subarray with nums[i]
            new_dp[x] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r]:
                    new_r = (r * x) % k
                    new_dp[new_r] += dp[r]

            dp = new_dp

            # Add all subarrays ending here to answer
            for r in range(k):
                ans[r] += dp[r]

        return ans