# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        res = root.val

        def dfs(node):
            nonlocal counter,res
            if not node: return
            
            #left
            dfs(node.left)

            if counter >=k: return #stop early; we alr found ans

            #current
            counter+=1
            if counter==k:
                res=node.val
                return
                
            #right   
            dfs(node.right)

        dfs(root)
        return res

            