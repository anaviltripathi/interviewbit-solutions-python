# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def pathSum(self, root, s):
        if not root:
            return []
        elif not root.left and not root.right:
            return [[root.val]] if root.val == s else []
        
        l = []
        
        for path in self.pathSum(root.left, s - root.val):
            l.append([root.val]+ path)
        
        for path in self.pathSum(root.right, s - root.val):
            l.append([root.val]+ path)
            
        return l

