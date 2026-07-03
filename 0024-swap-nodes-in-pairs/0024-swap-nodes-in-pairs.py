class Solution:
    def swapPairs(self, head):
        d = ListNode(0)
        d.next = head
        p = d
        while p.next and p.next.next:
            a = p.next
            b = a.next
            a.next = b.next
            b.next = a
            p.next = b
            p = a
        return d.next