class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX = 2048

        # prev[x] means:
        # XOR value x is possible after choosing the previous number of elements
        prev = [False] * MAX

        # Choosing 0 numbers gives XOR 0
        prev[0] = True

        # Build states for choosing 1, 2, and 3 numbers
        for _ in range(3):
            curr = [False] * MAX

            for x in range(MAX):
                if prev[x]:
                    for v in nums:
                        # Add a new number to the current XOR
                        curr[x ^ v] = True

            prev = curr

        # Count how many XOR values are possible after choosing 3 numbers
        return sum(prev)