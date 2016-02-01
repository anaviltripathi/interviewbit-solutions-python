# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        d = {}
        if not node:
            return node
        node2 = UndirectedGraphNode(node.label)
        d[node] = node2
        d[None] = None
        q = [node]
        
        while q:
            u = q.pop(0)
            for n in u.neighbors:
                if n not in d:
                    d[n] = UndirectedGraphNode(n.label)
                    q.append(n)
                d[u].neighbors.append(d[n])
                    
        return node2

