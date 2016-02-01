# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        import sys
        res = [-sys.maxint-1]
        self.maxPathSumHelper(A, res)
        return res[0]
        
    def maxPathSumHelper(self, A, res):
        if not A: return 0
        l_p = self.maxPathSumHelper(A.left, res)
        r_p = self.maxPathSumHelper(A.right, res)
        single = max(max(l_p, r_p) + A.val, A.val)
        both = max(l_p + r_p + A.val, single)
        res[0] = max(res[0], both)
        
        return single

