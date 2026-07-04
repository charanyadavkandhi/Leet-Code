from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        
        def isValid(st):
            cnt = 0
            for ch in st:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        q = deque([s])
        visited = {s}
        ans = []
        found = False

        while q:
            cur = q.popleft()

            if isValid(cur):
                ans.append(cur)
                found = True

            if found:
                continue

            for i in range(len(cur)):
                if cur[i] not in '()':
                    continue

                nxt = cur[:i] + cur[i+1:]

                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return ans