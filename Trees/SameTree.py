# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A == None and B == None: return True
        elif A == None or B == None: return False
        return A.val == B.val and self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)
        
