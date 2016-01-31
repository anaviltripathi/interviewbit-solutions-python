# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        if not A:
            return False
        curr1 = A
        curr2 = A
        s1 = []
        s2 = []
        done1 = False
        done2 = False
        while True:
            while not done1:
                #inorder 1
                if curr1:
                    s1.append(curr1)
                    curr1 = curr1.left
                else:
                    if not s1:
                        done1 = True
                        continue
                    curr1 = s1.pop()
                    val1 = curr1.val
                    curr1 = curr1.right
                    done1 = True
                    
                    
            while not done2:
                #inorder 2
                if curr2:
                    s2.append(curr2)
                    curr2 = curr2.right
                else:
                    if not s2:
                        done2 = True
                        continue
                    curr2 = s2.pop()
                    val2 = curr2.val
                    curr2 = curr2.left
                    done2 = True
            
            if val1 >= val2:
                return 0
            
            if val1 + val2 == B and val1 != val2:
                return 1
            
            if val1 + val2 < B:
                done1 = False
            elif val1 + val2 > B:
                done2 = False
            
            
                
                
                

