class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        # First and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Find the smallest valid substring for every character
        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                idx = ord(s[i]) - ord('a')

                # This character occurs before our current left
                if first[idx] < left:
                    valid = False
                    break

                # Include all occurrences of this character
                right = max(right, last[idx])
                i += 1

            if valid:
                intervals.append((left, right))

        # Choose intervals with earliest ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result