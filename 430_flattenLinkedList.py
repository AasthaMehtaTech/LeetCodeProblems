#fastest
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        pointer = head
        branches = []
        while pointer:
            if pointer.child:
                if pointer.next: branches.append(pointer.next)
                pointer.next = pointer.child
                pointer.child = None
                pointer.next.prev = pointer
            elif not pointer.next and len(branches) > 0:
                pointer.next = branches.pop()
                pointer.next.prev = pointer
            pointer = pointer.next
        
        return head
        
        
#stack for every situation
class Solution(object):

    def flatten(self, head):
        if not head:
            return head

        stack = []
        pseudo_head = Node(0, None, head, None)
        prev = pseudo_head
        stack.append(head)
        
        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
            head.prev = None
        return head
        
#oops
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

"""
root.next.prev =  last element of root.child 
root.child = root.next
child.prev = root

"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        dummy = head
        if not head:
            return head
        
        while head:
            if head.child:
                head = self.processChild(head)
            else:
                head = head.next
        return dummy
   
        
    def processChild(self,node):
        next = node.next
        node.next = node.child
        node.child.prev = node
        node.child = None
        
        while node.next:
            if node.child:
                self.processChild(node)
            node = node.next
            
        if next:
            next.prev = node
            node.next = next
            
        return node
        
#dfs
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head):
        if not head:
            return head

        # pseudo head to ensure the `prev` pointer is never none
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)

        # detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next


    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        # the curr.next would be tempered in the recursive function
        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)
                
