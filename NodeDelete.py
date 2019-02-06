class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None
        while node is not None:
            if node.next is not None:
                prev = node
                prev.next = node.next
                node.val = node.next.val
                node = node.next
            else:
                break
        prev.next = None
