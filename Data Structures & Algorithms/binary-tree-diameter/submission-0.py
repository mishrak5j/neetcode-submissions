# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def get_height(node):
            if not node:
                return 0

            left = get_height(node.left)
            right = get_height(node.right)

            self.max_diameter = max(self.max_diameter, left+right)

            return 1 + max(left,right)


        get_height(root)
        return self.max_diameter