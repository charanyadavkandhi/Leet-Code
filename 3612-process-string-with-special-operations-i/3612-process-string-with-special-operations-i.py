class Solution:
    def processStr(self, s: str) -> str:
        res = ""

        for ch in s:
            if ch.islower():
                res += ch
            elif ch == '*':
                res = res[:-1]
            elif ch == '#':
                res += res
            elif ch == '%':
                res = res[::-1]

        return res