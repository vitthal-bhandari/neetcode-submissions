# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def computePath(node):
            if not node:
                return 0
            leftPath = computePath(node.left)
            rightPath = computePath(node.right)
            res[0] = max(res[0], leftPath + rightPath)
            return max(leftPath, rightPath) + 1
        if not root:
            return 0
        computePath(root)
        return res[0]