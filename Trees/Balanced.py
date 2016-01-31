# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        return False if self.findheight(A, 0) == -1 else True
        
        
    def findheight(self, A, depth):
        if not A.left and not A.right : return depth
        
        left_height = 0
        right_height = 0
        
        if A.left:
            left_height = self.findheight(A.left , depth + 1)
            #print "left", A.left.val, depth
        if A.right:
            right_height = self.findheight(A.right, depth + 1)
            #print "right", A.right.val, depth
            
        if left_height == -1 or right_height == -1: 
            return -1
            
        if left_height - right_height > 1: 
            return -1
        else:
            return max(left_height, right_height)
        

