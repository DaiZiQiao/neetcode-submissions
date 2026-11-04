# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._inorderTraversal(root)


    def _inorderTraversal(self,root):
        res = []
        if root:
            res += self._inorderTraversal(root.left)
            res.append(root.val)
            res += self._inorderTraversal(root.right)
        return res

        
        
        

