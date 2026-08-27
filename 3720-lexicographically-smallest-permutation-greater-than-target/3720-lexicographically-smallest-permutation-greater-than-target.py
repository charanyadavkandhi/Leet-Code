class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = []

        # Match target as much as possible
        for i in range(len(target)):
            t = ord(target[i]) - ord('a')

            if cnt[t] > 0:
                ans.append(target[i])
                cnt[t] -= 1
            else:
                # Cannot match target[i].
                # Try to put a larger character here.
                for c in range(t + 1, 26):
                    if cnt[c] > 0:
                        ans.append(chr(c + ord('a')))
                        cnt[c] -= 1

                        # Smallest possible suffix
                        for x in range(26):
                            ans.extend([chr(x + ord('a'))] * cnt[x])

                        return ''.join(ans)

                # No larger character available.
                break

        # Backtrack through the matched prefix.
        # Restore characters one by one and try to increase that position.
        for i in range(len(ans) - 1, -1, -1):
            c = ord(ans[i]) - ord('a')
            cnt[c] += 1

            t = ord(target[i]) - ord('a')

            # Find smallest character greater than target[i]
            for x in range(t + 1, 26):
                if cnt[x] > 0:
                    result = ans[:i]
                    result.append(chr(x + ord('a')))
                    cnt[x] -= 1

                    # Add remaining characters in sorted order
                    for y in range(26):
                        result.extend([chr(y + ord('a'))] * cnt[y])

                    return ''.join(result)

        return ""