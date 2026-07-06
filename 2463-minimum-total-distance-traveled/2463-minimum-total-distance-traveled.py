class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        positions = []

        for pos, limit in factory:
            positions.extend([pos] * limit)

        n = len(robot)
        m = len(positions)

        dp = [float('inf')] * (m + 1)

        for j in range(m + 1):
            dp[j] = 0

        for i in range(1, n + 1):
            new_dp = [float('inf')] * (m + 1)

            for j in range(1, m + 1):
                new_dp[j] = min(
                    new_dp[j - 1],
                    dp[j - 1] + abs(robot[i - 1] - positions[j - 1])
                )

            dp = new_dp

        return dp[m]