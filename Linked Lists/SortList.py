# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        #partition the lists
        #merge them and return 
        return self.mergeSort(A)
        

    
    def mergeSort(self, A):
        if A.next == None : 
            return A
        else:
            p1, p2 = self.partitionList(A)
            p1 = self.mergeSort(p1)
            p2 = self.mergeSort(p2)
            A = self.mergeList(p1, p2)
            
            return A
            
    def mergeList(self, A, B):
        
        p1 = A
        p2 = B
        p1_prev = None
        while p1 and p2:
            if p1.val <= p2.val:
                p1_prev = p1
                p1 = p1.next
            else:
                if p1_prev != None : p1_prev.next = p2
                p1, p2 = p2, p1
        p1_prev.next = p2
        
        return A if A.val <= B.val else B
                

    def partitionList(self, A):
        curr = A
        halfway = A
        
        while curr:
            curr = curr.next
            if not curr: break
            prev = halfway
            halfway = halfway.next
            curr = curr.next
            
        prev.next = None
        return A, halfway

