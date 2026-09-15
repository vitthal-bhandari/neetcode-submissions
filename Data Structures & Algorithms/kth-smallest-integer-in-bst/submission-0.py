# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal k
            if not node:
                return -1
            leftVal = inorder(node.left)
            if leftVal != -1:
                return leftVal
            if k > 0:
                k -= 1
                if k == 0:
                    return node.val
            rightVal = inorder(node.right)
            if rightVal != -1:
                return rightVal
            return -1
        
        return inorder(root)