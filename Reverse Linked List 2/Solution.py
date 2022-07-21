# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        foundNodes = []
        
        dummy = ListNode(0, head)
        current = dummy.next #dummy array @ head of list
        
        count = 1
        
        while count <= right:
            if count >= left and count <= right: #check if count is withing out left and right range
                foundNodes.append(current)
            
            current = current.next # move to next node
            count += 1 #increase count
        
        #now we have a hashmap with values we can resort out list
        
        left, right = 0, len(foundNodes) - 1 # two pointers 
        while left < right:
            first = foundNodes[left]
            second = foundNodes[right]

            first.val, second.val = second.val, first.val
            left += 1
            right -= 1
        
        return dummy.next