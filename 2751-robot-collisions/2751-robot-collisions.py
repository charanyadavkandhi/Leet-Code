class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        robots = sorted(range(n), key=lambda i: positions[i])
        stack = []

        for i in robots:
            if directions[i] == 'R':
                stack.append(i)

            else:
                while stack and healths[i] > 0:
                    j = stack[-1]

                    if healths[j] < healths[i]:
                        healths[i] -= 1
                        healths[j] = 0
                        stack.pop()

                    elif healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0

                    else:
                        healths[j] = 0
                        healths[i] = 0
                        stack.pop()

        return [healths[i] for i in range(n) if healths[i] > 0]