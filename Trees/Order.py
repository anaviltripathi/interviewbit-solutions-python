class Solution:
    # @param heights : list of integers
    # @param infronts : list of integers
    # @return a list of integers
    
    def order(self, heights, infronts):
        h_i = zip(heights, infronts)
        sorted_heights = sorted(h_i)
        
        segment_tree = [[[0,0],0]] * 2 * (len(heights)+1) 
        
        segment_tree[0] = [[0, len(heights)-1], 0]
        
        for i in range(len(segment_tree)/2 - 1):
            l = segment_tree[i][0][0]
            r = segment_tree[i][0][1]
            segment_tree[2*i+ 1] = [[l, (r+l)/2], 0]
            segment_tree[2*i + 2] = [[(r+l)/2 + 1, r], 0]
        
        
        #print segment_tree 
        #print sorted_heights
        actual_order = ['-']*len(heights)
       
#	   s = segment_tree(len(heights))
       
        for i in range(len(sorted_heights)):
            #pos = s.findposition(sorted_heights[i])
            pos, segment_tree = self.findposition(segment_tree, 0, sorted_heights[i][1])
            #print pos
           #while k <= sorted_heights[i][1]:
           #    if actual_order[j] == '-':
           #        k += 1
           #    j += 1
            #print actual_order
            
            actual_order[pos] = sorted_heights[i][0]
      
        return actual_order
       
       
    def findposition(self, segment_tree, i, pos):
        segment_tree[i][1] += 1
        #print segment_tree[i][1]
        if segment_tree[i][0][0] == segment_tree[i][0][1]:
            #print 
            return segment_tree[i][0][0], segment_tree
        else:
            if segment_tree[2*i+1][0][1] - segment_tree[2*i+1][0][0] - segment_tree[2*i+1][1] >= pos:
                #print "going left ", segment_tree
                #print segment_tree[2*i+1][0][1], segment_tree[2*i+1][0][0], segment_tree[2*i+1][1], pos
                return self.findposition(segment_tree, 2*i + 1, pos)
                
            else:
                #print "going right ", segment_tree
                return self.findposition(segment_tree, 2*i + 2, pos - (segment_tree[2*i+1][0][1] + 1 - segment_tree[2*i+1][0][0] - segment_tree[2*i+1][1]))
                
                
                
#class segment_tree:
#    def __init__(self, N):
#        self.N = N
#        self.val = 0
#        self.left = None
#        self.right = None
#        
##        
 #   def findposition(self, pos):
 #       if (self.N)/2 == self.val: return .....
 #       
 #       if (self.N)/2 - self.val >= i:
 #           self.val += 1
 #           if not self.left:
 #               self.left = segment_tree(self.N/2)
 #           
 #           self.left.findposition(pos)
                
    
    
       
