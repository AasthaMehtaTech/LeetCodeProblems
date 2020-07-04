#fastest - recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1 
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            
        ''' 
        or------------
        
        out = ListNode()
        p = out
        
        while l1 and l2:
            
            if l1.val <= l2.val:
                out.next = l1
                l1 = l1.next
            else:
                out.next = l2
                l2 = l2.next
                
            out = out.next
        
        out.next = l1 if l1 else l2
                
        return p.next
        '''
        
        
#light
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newListRoot = None
        last = None
        
        p1 = l1
        p2 = l2
        while p1 is not None or p2 is not None:
            toPut = None
            if p1 is None:
                toPut = p2.val
                p2 = p2.next
            elif p2 is None:
                toPut = p1.val
                p1 = p1.next
            else:
                if p1.val < p2.val:
                    toPut = p1.val
                    p1 = p1.next
                else:
                    toPut = p2.val
                    p2 = p2.next
                    
            if last is None:
                newListRoot = ListNode(toPut)
                last = newListRoot
                
            else:
                last.next = ListNode(toPut)
                last = last.next
        
        return newListRoot
