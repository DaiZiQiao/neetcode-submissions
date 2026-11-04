# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        if head is None:
            return
        next_node = head.next
        head.next = None

        while next_node is not None:
            next_next = next_node.next
            next_node.next = curr_node
            curr_node = next_node
            next_node = next_next

        return curr_node


