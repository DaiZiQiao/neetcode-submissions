# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right_side = []
        queue = deque([root])
        while queue:
            level = len(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                if i == level - 1:
                    right_side.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
        return right_side
