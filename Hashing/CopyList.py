# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        from collections import defaultdict
        d = defaultdict(lambda: RandomListNode(0))
        d[None] = None
        m = head
        
        while m:
            d[m].label = m.label
            d[m].next = d[m.next]
            d[m].random = d[m.random]
            m = m.next
            
        return d[head]

