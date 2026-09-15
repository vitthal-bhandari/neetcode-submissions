# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def maxPath(node):
            nonlocal res
            if not node:
                return 0
            leftMax = maxPath(node.left)
            rightMax = maxPath(node.right)
            res = max(res, max(0, leftMax) + node.val + max(0, rightMax))
            return node.val + max(0, leftMax, rightMax)
        maxPath(root)
        return res