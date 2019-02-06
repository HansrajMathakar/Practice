# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    
        curr = head
        
        while curr is not None:
            runner = curr.next
            
            while runner != None and runner.val == curr.val:
                runner = runner.next
            
            curr.next = runner
            
            curr = curr.next
            
        return head
            
