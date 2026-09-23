class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1

        # If target == 0, remove every element
        if target == 0:
            return len(nums)

        left = 0
        curr_sum = 0
        max_len = -1

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        return -1 if max_len == -1 else len(nums) - max_len