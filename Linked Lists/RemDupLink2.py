# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        def removeDup(prev, curr):
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
            prev.next = curr.next
            return prev, curr.next
            
        if not head or not head.next:
            return head
        
        prev = head
        curr = head.next
        
        while curr and prev and prev.val == curr.val:
            while curr and prev and prev.val == curr.val:
                prev, curr = curr, curr.next
            if not curr:
                return curr
            prev = curr
            curr = curr.next
        
        head = prev
            
        while curr:
            if curr.next and curr.next.val == curr.val:
                prev, curr = removeDup(prev, curr)
                
            else:
                prev = curr
                curr = curr.next
                    
        return head
