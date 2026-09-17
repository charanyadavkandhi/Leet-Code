class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        
        best = [INF] * n
        left = 0
        curr_sum = 0
        ans = INF
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            if curr_sum == target:
                length = right - left + 1
                
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])
                
                best[right] = min(
                    length,
                    best[right - 1] if right > 0 else INF
                )
            else:
                best[right] = best[right - 1] if right > 0 else INF
        
        return -1 if ans == INF else ans