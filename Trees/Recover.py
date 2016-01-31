# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        import sys
        anomaly1 = None 
        anomaly2 = None
        last_value = - sys.maxint - 1 
        st = []
        #l = []
        st.append(A)
        while st:
            u = st[-1]
            #st = st[:-1]
            if u.right:
                st = st[:-1] + [u.right] + [st[-1]]
                u.right = None
            #st.append(u)
            if u.left: 
                st.append(u.left)
                u.left = None
            else:
                #print u
                st = st[:-1]
                if anomaly1 == None and last_value > u.val:
                    anomaly1 = last_value
                    #l.append(anomaly1)
                    last_value = u.val
                    anomaly1_next_val = u.val
                elif last_value < u.val:
                    last_value = u.val
                elif anomaly1 != None and last_value > u.val:
                    anomaly2 = u.val
                    #l.append(anomaly2)
                    break
                
                #print l
        if anomaly2 == None: return [anomaly1_next_val, anomaly1]
        else: return [anomaly2, anomaly1]
        
        
