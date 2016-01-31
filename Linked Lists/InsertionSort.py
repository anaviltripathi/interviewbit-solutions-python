# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head = A
        def insert_into_correct_place(head, curr, prev):
            if head.val > curr.val:
                prev.next = curr.next
                curr.next = head
                head = curr
                return curr, prev
                
            c = head
            while c.next.val < curr.val:
                c = c.next
            
            prev.next = curr.next
            curr.next = c.next
            c.next = curr
            return head, prev
            
        curr = head
        prev = None
        while curr:
            if prev and prev.val > curr.val:
                head, curr = insert_into_correct_place(head, curr, prev)
            
            prev = curr
            curr = curr.next
            
        return head
