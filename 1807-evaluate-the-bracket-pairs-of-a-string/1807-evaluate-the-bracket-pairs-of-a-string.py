class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge into a dictionary
        mp = dict(knowledge)

        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                # Find the closing bracket
                j = i + 1
                while s[j] != ')':
                    j += 1

                # Extract key
                key = s[i + 1:j]

                # Add value if known, otherwise '?'
                result.append(mp.get(key, '?'))

                # Move after ')'
                i = j + 1

            else:
                result.append(s[i])
                i += 1

        return ''.join(result)