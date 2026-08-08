class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # last[j] = position of word2[j] when matching word2
        # from right to left in word1
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        canSkip = True

        # Greedily choose the smallest possible index
        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed character change
            elif canSkip and (
                j == m - 1 or i < last[j + 1]
            ):
                ans.append(i)
                j += 1
                canSkip = False

        return ans if j == m else []