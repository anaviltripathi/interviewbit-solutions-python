# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        if A == None: return True
        return self.isSame(A.left, A.right)
    
    def isSame(self, A, B):
        if A == None and B == None: return True
        elif A == None or B == None: return False
        return A.val == B.val and self.isSame(A.left, B.right) and self.isSame(A.right, B.left)
    
    
