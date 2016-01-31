# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        l = []
        st = []
        st.append(A)
        while st:
            u = st[-1]
            l.append(u.val)
            st = st[:-1]
            if u.right: st.append(u.right)
            if u.left: st.append(u.left)
        
        
        return l

