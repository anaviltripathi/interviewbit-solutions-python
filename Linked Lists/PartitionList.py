# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        small_list = []
        large_list = []
        
        curr = A
        while curr:
            if curr.val < B:
                small_list.append(curr.val)
            else:
                large_list.append(curr.val)
            
            curr = curr.next
            
        i = 0
        curr = A
        while curr:
            if i < len(small_list):
                curr.val = small_list[i]
            else:
                curr.val = large_list[i-len(small_list)]
            curr = curr.next
            
            i += 1
            
        return A

