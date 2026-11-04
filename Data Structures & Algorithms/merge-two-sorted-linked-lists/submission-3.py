# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        tail = new_head

        curr1 = list1
        curr2 = list2

        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next

        if curr1 is not None:
            tail.next = curr1
        elif curr2 is not None:
            tail.next = curr2

        return new_head.next
