# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        head = A
        def findMidandReverse(head):
            if not head or not head.next:
                return head, head
            curr1 = head
            curr2 = head
            
            while curr1 and curr2:
                curr2 = curr2.next
                if curr2:
                    curr2 = curr2.next
                prev = curr1
                curr1 = curr1.next
            
            ##Found Mid now reversing
            p = curr1
            c = curr1.next
            while c:
                c.next , p,  c = p, c, c.next
            
            curr1.next = None
            return head, p
            
            
        c1, c2 = findMidandReverse(head)
            
        while c1 and c2:
            if c1.val == c2.val:
                c1 = c1.next
                c2 = c2.next
            else:
                return 0
            
        return 1
