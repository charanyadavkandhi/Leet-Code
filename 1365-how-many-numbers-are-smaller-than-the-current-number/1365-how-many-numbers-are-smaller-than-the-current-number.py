class Solution:
    def smallerNumbersThanCurrent(self, nums):
        return [sum(x < num for x in nums) for num in nums]