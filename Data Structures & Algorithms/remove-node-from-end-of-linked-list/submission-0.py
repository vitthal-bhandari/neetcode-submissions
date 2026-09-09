# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        temp = head
        while temp:
            temp = temp.next
            l += 1
        if l - n == 0:
            return head.next
        temp = head
        i = 0
        while temp:
            if i == l-n-1:
                # skip next node
                temp.next = temp.next.next
            i += 1
            temp = temp.next
        return head