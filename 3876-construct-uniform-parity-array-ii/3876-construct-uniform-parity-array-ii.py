class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        has_even = False

        for x in nums1:
            if x % 2 == 0:
                has_even = True
            else:
                min_odd = min(min_odd, x)

        # All numbers are even
        if min_odd == float('inf'):
            return True

        # All numbers are odd
        if not has_even:
            return True

        # Every even number must have a smaller odd number
        for x in nums1:
            if x % 2 == 0 and x <= min_odd:
                return False

        return True