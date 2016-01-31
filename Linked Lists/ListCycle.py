# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        p1 = A
        p2 = A
        
        first_time = 1
        while first_time == 1 or p1 != p2:
            p1 = p1.next
            if p2 == None or p2.next == None:
                return None
            else:
                p2 = p2.next.next
            
            first_time = 0
        
        #print "yaha a gya bc"
        p1 = A
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        
        return p2
            

