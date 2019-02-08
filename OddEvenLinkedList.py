# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: 'ListNode') -> 'ListNode':
        
        if head is None or head.next is None or head.next.next is None:
            return head
        
        odd = head
        even = head.next
        curr = head.next 
        
        while odd.next and even.next:
            if odd.next and odd.next.next:
                odd.next = odd.next.next
                odd = odd.next
                
            if even.next and even.next.next:
                even.next = even.next.next
                even = even.next
        
        even.next = None
        odd.next = curr
        return head
