# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            # Best contribution from left and right subtrees.
            # If a subtree hurts the sum, ignore it by taking 0.
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Best complete path that passes through this node
            current_path = node.val + left + right

            # Update global answer
            max_sum = max(max_sum, current_path)

            # Return the best ONE-sided path to the parent
            return node.val + max(left, right)

        dfs(root)
        return max_sum

