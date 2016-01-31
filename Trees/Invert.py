# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @return the root node in the tree
    def invertTree(self, root):
        if root == None: return None
        elif root.left == None and root.right == None: return root
        else:
            root.left , root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            
        return root

