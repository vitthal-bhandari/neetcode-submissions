# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minH = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minH, (lists[i].val, i))
        res = ListNode()
        dummy = res
        while minH:
            val, nextIdx = heapq.heappop(minH)
            lists[nextIdx] = lists[nextIdx].next
            if lists[nextIdx]:
                heapq.heappush(minH, (lists[nextIdx].val, nextIdx))
            dummy.next = ListNode(val)
            dummy = dummy.next
        return res.next