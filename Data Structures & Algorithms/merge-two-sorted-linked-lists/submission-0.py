# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        initial = ListNode()
        head = initial
        while list1 and list2:
            if list1.val <= list2.val:
                initial.next = list1
                list1 = list1.next
            else:
                initial.next = list2
                list2 = list2.next
            initial = initial.next
        if list1:
            initial.next = list1
        if list2:
            initial.next = list2
        return head.next