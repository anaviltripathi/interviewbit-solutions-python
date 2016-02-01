# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        ar = []
        curr = A
        while curr:
            ar.append(curr.val)
            curr = curr.next
            
        def constructBST(l):
            if not l:
                return None
            
            mid = len(l)/2
            root = TreeNode(l[mid])
            root.left = constructBST(l[:mid])
            root.right = constructBST(l[mid+1:])
            
            return root
            
        return constructBST(ar)

