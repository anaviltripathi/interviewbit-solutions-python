# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        count = 0
        return self.maxDepthHelper(A, count)
    
    def maxDepthHelper(self, A, count):
        count += 1
        l = count
        r = count
        if A.left: l = self.maxDepthHelper(A.left, count)
        if A.right: r = self.maxDepthHelper(A.right, count)
        
        return max(l,r)
        

