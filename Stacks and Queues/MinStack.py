class MinStack:
    # @param x, an integer
    
    def __init__(self):
        self.st = []
        
    
    def push(self, x):
        if not self.st:
            self.st.append((x, 0))
            
        else:
            if x < self.st[self.st[-1][1]][0]:
                self.st.append((x, len(self.st)))
        
            else:
                self.st.append((x, self.st[-1][1]))
            
        
    # @return nothing
    def pop(self):
        if self.st != []: self.st.pop()
        


    # @return an integer
    def top(self):
        if not self.st: return -1 
        else:
            return self.st[-1][0]
        


    # @return an integer
    def getMin(self):
        if not self.st : return -1 
        else:
            return self.st[self.st[-1][1]][0]
        



