class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        cur = 0
        down = False

        for ch in s:
            rows[cur] += ch

            if cur == 0 or cur == numRows - 1:
                down = not down

            cur += 1 if down else -1

        return ''.join(rows)