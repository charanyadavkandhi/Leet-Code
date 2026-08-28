class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd = [i for i in range(26) if cnt[i] & 1]
        if n % 2 == 0:
            if odd:
                return ""
            mid_idx = -1
        else:
            if len(odd) != 1:
                return ""
            mid_idx = odd[0]

        m = n // 2
        pool = [cnt[i] // 2 for i in range(26)]
        H = [''] * m
        t = m
        for i in range(m):
            idx = ord(target[i]) - 97
            if pool[idx] > 0:
                pool[idx] -= 1
                H[i] = target[i]
            else:
                t = i
                break

        def fill_ascending(start):
            j = start
            for c in range(26):
                while pool[c] > 0:
                    H[j] = chr(c + 97)
                    pool[c] -= 1
                    j += 1

        def backtrack(start_i):
            i = start_i
            while i >= 0:
                tidx = ord(target[i]) - 97
                best = -1
                for c in range(tidx + 1, 26):
                    if pool[c] > 0:
                        best = c
                        break
                if best != -1:
                    pool[best] -= 1
                    H[i] = chr(best + 97)
                    fill_ascending(i + 1)
                    return True
                if i == 0:
                    return False
                pidx = ord(H[i - 1]) - 97
                pool[pidx] += 1
                i -= 1
            return False

        success = False

        if t == m:
            leaf_result = None
            pos = m
            if mid_idx != -1:
                mc = chr(mid_idx + 97)
                if mc > target[m]:
                    leaf_result = True
                elif mc < target[m]:
                    leaf_result = False
                pos = m + 1
            if leaf_result is None:
                for k in range(m):
                    hc = H[m - 1 - k]
                    tc = target[pos + k]
                    if hc > tc:
                        leaf_result = True
                        break
                    elif hc < tc:
                        leaf_result = False
                        break
                if leaf_result is None:
                    leaf_result = False  # exactly equal -> not strictly greater

            if leaf_result:
                success = True
            else:
                if m > 0:
                    idx_last = ord(H[m - 1]) - 97
                    pool[idx_last] += 1
                    success = backtrack(m - 1)
                else:
                    success = False
        else:
            success = backtrack(t)

        if not success:
            return ""

        mid_str = chr(mid_idx + 97) if mid_idx != -1 else ""
        return ''.join(H) + mid_str + ''.join(reversed(H))