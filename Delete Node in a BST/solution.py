# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return None

        if key < node.val:
            node.left = self.deleteNode(node.left, key)
            return node

        if key > node.val:
            node.right = self.deleteNode(node.right, key)
            return node

        if not node.left:
            return node.right

        if not node.right:
            return node.left

        next_bigger = node.right

        while next_bigger.left:
            next_bigger = next_bigger.left

        node.val = next_bigger.val

        node.right = self.deleteNode(node.right, next_bigger.val)

        return node
