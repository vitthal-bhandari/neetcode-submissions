"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        initial = head
        while initial:
            oldToNew[initial] = Node(initial.val)
            initial = initial.next
        node = head
        while node:
            oldToNew[node].random = oldToNew.get(node.random)
            oldToNew[node].next = oldToNew.get(node.next)
            node = node.next
        return oldToNew.get(head)
