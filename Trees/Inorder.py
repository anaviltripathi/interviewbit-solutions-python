# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        import sys
        
        l = []
        st = []
        st.append((A, A.val))
        while st:
            u, val = st[-1]
            #st = st[:-1]
            if u.right:
                st = st[:-1] + [(u.right, u.right.val)] + [st[-1]]
                u.right = None
            #st.append(u)
            if u.left: 
                st.append((u.left, u.left.val))
                u.left = None
            else:
                #print u
                st = st[:-1]
                l.append(val)
                #print l
                
        return l
