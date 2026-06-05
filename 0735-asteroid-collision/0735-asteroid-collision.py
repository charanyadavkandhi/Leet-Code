class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:

                # top asteroid smaller -> destroy it
                if stack[-1] < -ast:
                    stack.pop()
                    continue

                # equal size -> both destroyed
                elif stack[-1] == -ast:
                    stack.pop()

                # current asteroid destroyed
                break
            else:
                stack.append(ast)

        return stack