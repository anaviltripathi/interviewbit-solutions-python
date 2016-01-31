# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.st = []
        self.pushAllLeft(root)
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if self.st else False
        

    # @return an integer, the next smallest number
    def next(self):
        temp = self.st.pop()
        self.pushAllLeft(temp.right)
        return temp.val
        
    def pushAllLeft(self, root):
        if root:
            self.st.append(root)
            
            while root.left:
                self.st.append(root.left)
                root = root.left
        

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),

