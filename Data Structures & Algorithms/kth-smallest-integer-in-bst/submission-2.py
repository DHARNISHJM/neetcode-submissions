# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root, count, k):
        if root is not None:
            left_res = self.inorder(root.left, count, k)
            if left_res is not None:
                return left_res
            count[0] += 1
            if count[0] == k:
                return root.val
            right_res = self.inorder(root.right, count, k)
            if right_res is not None:
                return right_res
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorder(root, [0], k)
        