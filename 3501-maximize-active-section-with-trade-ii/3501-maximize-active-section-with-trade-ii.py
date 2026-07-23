from dataclasses import dataclass
from typing import List


@dataclass
class Group:
    start: int
    length: int


class SparseTable:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        if self.n == 0:
            self.st = []
            return

        k = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(k)]
        self.st[0] = nums[:]

        j = 1
        while (1 << j) <= self.n:
            length = 1 << j
            half = length >> 1
            for i in range(self.n - length + 1):
                self.st[j][i] = max(self.st[j - 1][i],
                                    self.st[j - 1][i + half])
            j += 1

    def query(self, l: int, r: int) -> int:
        if l > r:
            return 0
        k = (r - l + 1).bit_length() - 1
        return max(self.st[k][l], self.st[k][r - (1 << k) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = s.count("1")

        zero_groups, zero_group_index = self._get_zero_groups(s)

        if not zero_groups:
            return [ones] * len(queries)

        merge = self._get_merge_lengths(zero_groups)
        st = SparseTable(merge)

        ans = []

        for l, r in queries:
            if zero_group_index[l] == -1:
                left = -1
            else:
                g = zero_groups[zero_group_index[l]]
                left = g.length - (l - g.start)

            if zero_group_index[r] == -1:
                right = -1
            else:
                g = zero_groups[zero_group_index[r]]
                right = r - g.start + 1

            start_adj = zero_group_index[l] + 1
            end_group = zero_group_index[r] if s[r] == "1" else zero_group_index[r] - 1
            end_adj = end_group - 1

            best = ones

            if (
                s[l] == "0"
                and s[r] == "0"
                and zero_group_index[l] + 1 == zero_group_index[r]
            ):
                best = max(best, ones + left + right)

            elif start_adj <= end_adj:
                best = max(best, ones + st.query(start_adj, end_adj))

            if (
                s[l] == "0"
                and zero_group_index[l] + 1
                <= (zero_group_index[r] if s[r] == "1" else zero_group_index[r] - 1)
            ):
                best = max(
                    best,
                    ones + left + zero_groups[zero_group_index[l] + 1].length,
                )

            if s[r] == "0" and zero_group_index[l] < zero_group_index[r] - 1:
                best = max(
                    best,
                    ones + right + zero_groups[zero_group_index[r] - 1].length,
                )

            ans.append(best)

        return ans

    def _get_zero_groups(self, s: str):
        groups = []
        idx = []

        for i, ch in enumerate(s):
            if ch == "0":
                if i > 0 and s[i - 1] == "0":
                    groups[-1].length += 1
                else:
                    groups.append(Group(i, 1))
            idx.append(len(groups) - 1)

        return groups, idx

    def _get_merge_lengths(self, groups):
        res = []
        for i in range(len(groups) - 1):
            res.append(groups[i].length + groups[i + 1].length)
        return res