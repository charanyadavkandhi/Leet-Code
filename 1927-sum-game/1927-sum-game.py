class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        diff = 0
        q1 = 0
        q2 = 0

        for i in range(half):
            if num[i] == '?':
                q1 += 1
            else:
                diff += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                q2 += 1
            else:
                diff -= int(num[i])

        # Odd number of '?' means Alice gets the extra move
        if (q1 + q2) % 2 == 1:
            return True

        # Alice wins if the final balanced value cannot be zero
        return diff + 9 * (q1 - q2) // 2 != 0