# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, root):
        level = []
        queue = []
        if root:
            queue.append(root)
        res = []
        while queue:
            new_queue = []
            res.append([])
            for node in queue:
                res[-1].append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
            
        return res

