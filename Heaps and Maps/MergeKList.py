# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        import heapq
        import sys
        
        k = []
        merged_list = None
        
        for a in A:
            heapq.heappush(k, (a.val, a))
        
        
        curr = k[0][1]
        merged_list = ListNode(curr.val) 
        merged_last = merged_list
        
        while curr:
            least_node_val = sys.maxint
            least_node = None
            
            heapq.heappop(k)
            
            if curr.next: heapq.heappush(k , (curr.next.val, curr.next))
            if not k: break
            curr = k[0][1]
            
            merged_last.next = ListNode(curr.val)
            merged_last = merged_last.next

        
        return merged_list
        
