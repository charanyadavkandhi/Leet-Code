class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # We have exactly k ones
            while ones == k:
                curr = s[left:right + 1]

                # Update shortest or lexicographically smallest
                if ans == "" or len(curr) < len(ans) or (
                    len(curr) == len(ans) and curr < ans
                ):
                    ans = curr

                # Move left to find a shorter window
                if s[left] == '1':
                    ones -= 1
                left += 1

        return ans