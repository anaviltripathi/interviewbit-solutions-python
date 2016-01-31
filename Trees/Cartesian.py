# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if not A:
            return None
            
        else:
            max_val= max(A)
            max_idx = A.index(max_val)
            root = TreeNode(max_val)
            root.left = self.buildTree(A[:max_idx])
            root.right = self.buildTree(A[max_idx+1:])
            
            return root

