# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        if A.left == None and A.right == None: 
            return A
        elif A.left == None:
            self.flatten(A.right)
            return A
        elif A.right == None:
            A.right = self.flatten(A.left)
            A.left = None
            return A
        else:
            l = self.flatten(A.left)
            A.left = None
            r = A.right
            last = self.findRightMost(l)
            last.right = self.flatten(r)
            A.right = l
            return A
        
    
    def findRightMost(self, A):
        #if A.left != None: print "WTF", A.val
        if A == None: return None
        curr = A
        while curr.right != None:
            curr = curr.right
        return curr

