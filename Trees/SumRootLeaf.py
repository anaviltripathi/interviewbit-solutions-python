# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, root):
        
        def helper(root,val):
            if root:
                if not (root.left or root.right):
                    res[0] += (val*10 + root.val) 
                if root.left:
                    helper(root.left, val*10 + root.val)
                if root.right:
                    helper(root.right, val*10 + root.val)
                
        if not root:
            return 0
        res = [0]
        helper(root, 0)
        return res[0]%1003

