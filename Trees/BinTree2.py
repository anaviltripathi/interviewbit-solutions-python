# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder : list of integers denoting preorder traversal of tree
    # @param inorder : list of integers denoting inorder traversal of tree
    # @return the root node in the tree
    def buildTree(self, preorder, inorder):
        def helper(l,r):
            root = None
            if l < r:
                i = d[preorder.pop(0)]
                root = TreeNode(inorder[i])
                root.left = helper(l,i)
                root.right = helper(i+1, r)
            
            return root
            
        d = {val:i for i, val in enumerate(inorder)}
        return helper(0, len(inorder))

