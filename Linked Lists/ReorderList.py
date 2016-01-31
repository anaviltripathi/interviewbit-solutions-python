# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        #if empty list or single node return it as it is
        head = A
        if head and head.next:
            
        
        #find middle element    
            #length = 0
            curr = head
            curr2 = head
            while curr:
                curr = curr.next
                prev = curr2
                if curr:
                    curr = curr.next
                    curr2 = curr2.next
                    prev = curr2
                else:
                    prev = curr2


            prev_p1 = head
            prev_p2 = self.reverseList(prev) #reverse the second half of list 
            curr_p1 = prev_p1.next
            curr_p2 = prev_p2.next
            
            if curr_p1 == prev_p2:
                return head
                pass
            else:
                while curr_p1 and curr_p2:
                    prev_p1.next = prev_p2
                    prev_p2.next = curr_p1
                    prev_p1 = curr_p1
                    prev_p2 = curr_p2
                    curr_p2 = curr_p2.next
                    curr_p1 = curr_p1.next
            
        return head
        
    def reverseList(self, head):
        if not head or not head.next:
            return head
            
        prev = head
        curr = head.next
        
        prev.next = None
        
        while prev and curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev

