# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        pos = 1

        first = -1
        last = -1
        minDist = float('inf')
        maxDist = -1

        while curr.next:
            nxt = curr.next

            # Local maximum or local minimum
            if ((curr.val > prev.val and curr.val > nxt.val) or
                (curr.val < prev.val and curr.val < nxt.val)):

                if first == -1:
                    first = pos
                else:
                    minDist = min(minDist, pos - last)
                    maxDist = pos - first

                last = pos

            prev = curr
            curr = nxt
            pos += 1

        # Fewer than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]

        return [minDist, maxDist]