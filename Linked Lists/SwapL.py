# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, head):
        if not head or not head.next:
            return head
            
        pre_prev = None
        prev = head
        curr = head.next
        nex = curr.next
        head = curr
        while curr:
            if pre_prev: 
                #print "fuck" 
                pre_prev.next = curr
            prev.next = nex
            curr.next = prev
            pre_prev = prev
            prev = nex
            if nex:
                curr = nex.next
                if curr: nex = curr.next
                else: break
            else:
                break
        
        return head

