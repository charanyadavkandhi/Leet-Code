class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, open_cnt, close_cnt):
            if len(s) == 2 * n:
                res.append(s)
                return

            if open_cnt < n:
                backtrack(s + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                backtrack(s + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return res