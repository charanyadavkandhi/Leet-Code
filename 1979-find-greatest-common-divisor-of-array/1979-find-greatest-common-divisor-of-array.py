class Solution:
    def findGCD(self, nums):
        a, b = min(nums), max(nums)
        while b:
            a, b = b, a % b
        return a