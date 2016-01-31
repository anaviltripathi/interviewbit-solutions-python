# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param val1 : integer
    # @param val2 : integer
    # @return an integer
    import copy
    
    def findval(self,A, val, path):
        if not A: return -1
        else:
            if A.val == val:
                return path + [A.val]
            else:
                pl = self.findval(A.left, val, path + [A.val])
                if pl != -1: return pl
                
                pr = self.findval(A.right, val, path + [A.val])
                if pr != -1: return pr
                
                return -1
                
                
    def lca(self, A, val1, val2):
        #return "fuck"
        p1 = self.findval(A, val1, [])
        p2 = self.findval(A, val2, [])
        
        if p1 == -1 or p2 == -1: return -1
        
        i = 0
        while i < len(p1) and i < len(p2) and p1[i] == p2[i]:
            i +=1 
            #print i
        
        return p1[i-1]
                    
                    
