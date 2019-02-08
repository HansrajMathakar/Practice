# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        
        d = {i: 1 for i in G}
        
        print(d)
        
        res = []
        
        while head:
            current = []
            while head and head.val in d:
                current.append(head.val)
                head = head.next
                
            if current:
                res.append(current)
                
            if head:
                head = head.next
        
        return len(res)
            
