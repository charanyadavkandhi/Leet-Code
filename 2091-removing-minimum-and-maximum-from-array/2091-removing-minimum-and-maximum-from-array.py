class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Remove both from front
        front = right + 1

        # Remove both from back
        back = n - left

        # Remove one from front and one from back
        both = (left + 1) + (n - right)

        return min(front, back, both)