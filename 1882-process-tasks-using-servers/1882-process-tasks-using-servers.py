
import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        current_time = 0

        for j, task in enumerate(tasks):

            # Time cannot go backwards
            current_time = max(current_time, j)

            # Release all available servers
            while busy and busy[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If all servers are busy, jump to earliest free time
            if not available:
                current_time = busy[0][0]

                # Release all servers free at this time
                while busy and busy[0][0] <= current_time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select the server with minimum weight and index
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Assign the task
            heapq.heappush(
                busy,
                (current_time + task, weight, index)
            )

        return ans
