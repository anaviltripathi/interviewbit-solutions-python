# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        left_q = []
        left_q.append(A)
        right_q = []
        left = True
        traversal = []
        curr_traverse = []
        while left_q or right_q:
            if left:
                curr = left_q[-1]
                curr_traverse.append(curr.val)
                left_q.pop()
                
                if curr.left: right_q.append(curr.left)
                if curr.right: right_q.append(curr.right)
                if not left_q:
                    left = False
                    traversal.append(curr_traverse)
                    curr_traverse = []
            else:
                curr = right_q[-1]
                curr_traverse.append(curr.val)
                right_q.pop()
                if curr.right: left_q.append(curr.right)
                if curr.left: left_q.append(curr.left)
                if not right_q:
                    left = True
                    traversal.append(curr_traverse)
                    curr_traverse = []
                    
                    
        
        return traversal
                    
                    
                
            
            

