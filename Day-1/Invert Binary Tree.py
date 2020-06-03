"""
Name of the problem :- Invert Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        left  = root.left
        right = root.right

        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root
    
sol = Solution()


def preorder(node):
    if not node:
        return 
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)