# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        head = A
        if A.next == None: return A
        start_prev = self.search_node(A,m-1)
        if start_prev == None:
            start = A
            part_list_head = self.reverseListTill_n(start, n - m + 1)
            return part_list_head
        else:
            start = start_prev.next
            part_list_head = self.reverseListTill_n(start, n - m + 1)
            start_prev.next = part_list_head
        #print(start_prev.val)
        #check what should be the starting node
        
        
        
        return head
        
    def reverseListTill_n(self, A, n):
        if A == None: return None
        elif A.next == None: return A
        else:
            count = 1
            start = A
            prev = A
            curr = A.next
            while count < n:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count += 1
            A.next = curr
            return prev
            
        
    def search_node(self, A, m):
        if m == 0: return None
        count = 1
        curr = A
        while count < m:
            curr = curr.next 
            count += 1
            
        return curr

