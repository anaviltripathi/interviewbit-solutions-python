# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, root, target):
        '''
        if not A:
            return 0
        return self.helper(A, B)
    
    def helper(self, root, target):    
        
        if root:
            if not root.left and not root.right:
                if target == root.val:
                    return 1
                else:
                    return 0
                    
            if root.left:
                if self.helper(root.left, target-root.val):
                    return 1
            if root.right:
                if self.helper(root.right, target-root.val):
                    return 1
            
            return 0
                    
        '''
        
        if not root:
            return 0
        else:
            target -= root.val
            if not (root.left or root.right):
                return 1 if not target else 0
            if root.left:
                if self.hasPathSum(root.left, target):
                    return 1
            if root.right:
                if self.hasPathSum(root.right, target):
                    return 1
            
            return 0

