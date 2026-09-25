class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def combine(A, B):
            return {a + b for a in A for b in B}

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    # Parse inside braces
                    sub, i = parse(i + 1)
                    current = combine(current, sub)

                elif expression[i] == ',':
                    # Union current expression into result
                    result |= current
                    current = {""}
                    i += 1

                else:
                    # Single lowercase letter
                    current = combine(current, {expression[i]})
                    i += 1

            # Add the final part
            result |= current

            # Skip closing '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)