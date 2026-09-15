# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def getHeight(node):
            if not node:
                return 0
            leftH = getHeight(node.left)
            rightH = getHeight(node.right)
            if leftH == -1 or rightH == -1 or abs(leftH - rightH) > 1:
                return -1
            return max(leftH, rightH) + 1
        return True if getHeight(root) != -1 else False