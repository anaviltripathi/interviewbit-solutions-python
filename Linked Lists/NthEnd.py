# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        head, n = A, B
        prev1 = None
        prev2 = None
        count = 0
        curr1, curr2 = head, head
        while curr2:
            count += 1
            if count > n:
                prev1 = curr1
                curr1 = curr1.next
            prev2 = curr2
            curr2 = curr2.next
            
        if prev1:
            if curr1:
                prev1.next = curr1.next
            else:
                prev1.next = None
        else:
            head = head.next
        
        return head

