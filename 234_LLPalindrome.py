#TC- O(n), SC- O(1)
#fastest
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        prev = None
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            next = slow.next
            
            #reversing first half of array logic
                     
            slow.next = prev
            prev = slow
            slow = next
            
        if fast != None:
            slow = slow.next
        
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True
        
        
        
#short 
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
