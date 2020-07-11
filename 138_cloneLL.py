#using buil-in fn
return copy.deepcopy(head)

#approach: 1. Make mirror node, 2. Attach .random values ,3. Seperate copied list by skipping 1 node.
#https://leetcode.com/problems/copy-list-with-random-pointer/discuss/614624/Python-O(n)-by-mirror-node-85%2B-w-Visualization


#fastest
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        m = n = head
        while m:
            dic[m] = Node(m.val)
            m = m.next
        #this
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        
        return dic.get(head)
'''        
        #or this
        curr = head
        while curr:
            if curr.random:
                dic[curr].random = dic[curr.random]
            if curr.next:
                dic[curr].next = dic[curr.next]
            curr = curr.next
        
        return dic[head]
        
'''

#recursion
class Solution:
    def __init__(self):
        self.visited = {}
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        if head in self.visited:
            return self.visited[head]
        
        node = Node(head.val, None, None)
        self.visited[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
        
#another recursion: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/627637/Python-Recursive-Solution-Time-O(n)-and-Space-O(n)


#iterative

class Solution:
    def __init__(self):
        self.visited = {}
        
    def getClonedNode(self,head):
        
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        
        
        self.visited[head] = Node(head.val)
        return self.visited[head]
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        #iterative
        if not head:
            return None
        
        new_head = Node(head.val)
        old_head = head
        self.visited[head] = new_head
        while old_head:
            
            new_head.random = self.getClonedNode(old_head.random)
            new_head.next = self.getClonedNode(old_head.next)
            
            new_head = new_head.next
            old_head = old_head.next
        
        return self.visited[head]
