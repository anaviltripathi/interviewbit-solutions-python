# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        l1, l2 = A, B
        carry = 0
        head = ListNode(0)
        curr = head
        while l1 or l2 or carry:
            if l1 and l2:
                curr.val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                curr.val = l1.val + carry
                l1 = l1.next
            elif l2:
                curr.val = l2.val + carry
                l2 = l2.next
            else:
                curr.val = carry
                carry = 0
                
            if curr.val > 9:
                carry = curr.val/10
                curr.val = curr.val%10
            else:
                carry = 0
            
            curr.next = ListNode(0)
            prev = curr
            curr = curr.next
            
        
        prev.next = None
        
        return head
