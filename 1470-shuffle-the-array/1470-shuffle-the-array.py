class Solution:
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.extend([nums[i], nums[i + n]])
        return result