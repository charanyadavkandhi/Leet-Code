from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        index = {num: i for i, num in enumerate(sorted_nums)}

        swaps = 0
        visited = [False] * len(nums)

        for i in range(len(nums)):
            if visited[i] or index[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = index[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps