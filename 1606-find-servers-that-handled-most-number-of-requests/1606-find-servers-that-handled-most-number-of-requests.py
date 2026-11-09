
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        import heapq
        from sortedcontainers import SortedList

        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            # Release servers whose requests are completed
            while busy and busy[0][0] <= arrival[i]:
                end_time, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            # Find the first available server >= i % k
            server = available.bisect_left(i % k)

            # Wrap around if necessary
            if server == len(available):
                server = 0

            selected = available.pop(server)

            # Assign request
            count[selected] += 1
            heapq.heappush(
                busy,
                (arrival[i] + load[i], selected)
            )

        max_requests = max(count)

        return [i for i in range(k) if count[i] == max_requests]
