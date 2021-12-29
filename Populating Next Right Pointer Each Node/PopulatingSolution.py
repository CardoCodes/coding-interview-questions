"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from typing import Collection


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        #append the root of the q
        q = Collection.deque()
        q.append(root)
        
        #while loop to 
        while q:
            curr = q.popleft()
            
            #we could assume that both exists at all time because its a perfect binary tree
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                
                q.append(curr.left)
                q.append(curr.right)
            
            else:
                return root
        return root
            
                