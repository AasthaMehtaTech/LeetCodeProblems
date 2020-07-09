#fastest
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #evaluate the length
        if not head:
            return 
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
        k %= length
        p = head
        for i in range(length-k-1):
            p = p.next
        newhead = p.next
        if not newhead:
            return head
        p.next = None
        cur.next = head
        return newhead
