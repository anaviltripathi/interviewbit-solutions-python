# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        head1 = A
        head2 = B
        
        p1 = head1
        p2 = head2
        
        p1_prev = None
        while p1 and p2:
            if p1.val <= p2.val:
                p1_prev = p1
                p1 = p1.next
            else:
                if p1_prev != None : p1_prev.next = p2
                p1, p2 = p2, p1
        p1_prev.next = p2
            
        return head1 if head1.val <= head2.val else head2

