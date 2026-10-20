class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        # pre[i] = number of descents (nums[j] > nums[j+1]) with j < i
        pre = [0] * (n + 1)
        for i in range(n - 1):
            pre[i + 1] = pre[i] + (1 if nums[i] > nums[i + 1] else 0)
        pre[n] = pre[n - 1] if n > 0 else 0

        # nd[i] = first index j >= i with nums[j] > nums[j+1], else n
        nd = [n] * (n + 1)
        for i in range(n - 2, -1, -1):
            nd[i] = i if nums[i] > nums[i + 1] else nd[i + 1]

        ans = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            prev_max = 0
            ok = True
            for s in range(0, n, k):
                e = s + k - 1
                d = pre[e] - pre[s]  # descents strictly inside the block
                if d == 0:
                    mn, mx = nums[s], nums[e]
                elif d == 1:
                    p = nd[s]
                    # block must be a rotation of a sorted sequence:
                    # the wrap-around (last -> first) must not be a descent
                    if nums[e] > nums[s]:
                        ok = False
                        break
                    mn, mx = nums[p + 1], nums[p]
                else:
                    ok = False
                    break
                if mn < prev_max:
                    ok = False
                    break
                prev_max = mx
            if ok:
                ans += k
        return ans