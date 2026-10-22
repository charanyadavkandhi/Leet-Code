class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        k = nums.index(0)

        asc = all(nums[(i + 1) % n] == (nums[i] + 1) % n for i in range(n))
        if asc:
            # rotate left k times, or reverse + rotate left (n-k) + reverse
            return min(k, n - k + 2)

        desc = all(nums[(i + 1) % n] == (nums[i] - 1) % n for i in range(n))
        if desc:
            # reverse first, then rotate left (n-1-k)
            a = 1 + (n - 1 - k)
            # rotate left so n-1 is at the front, then reverse
            b = (k + 1) % n + 1
            return min(a, b)

        return -1