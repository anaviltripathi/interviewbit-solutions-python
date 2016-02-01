class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        xcount = 0
        pos = []
        
        for i in range(len(A)):
            if A[i] == 'x':
                xcount += 1
                pos.append(i)
        
        if xcount == 0: return 0
        elif xcount == len(A): return 0
        
        centre_of_mass = pos[len(pos)/2]
        
        #print "centre of mass: ", centre_of_mass
        
        for i in range(centre_of_mass, -1, -1):
            start = i
            if A[i] != 'x':
                break
        
        for i in range(centre_of_mass, len(A)):
            max_i = i
            if A[i] != 'x':
                break
          
        start += 1
        max_i -= 1
        
        #print "start: ", start
        #print "end: ", max_i
        
        ldist = 0
        if start != 0:
            count = 0
            
            for i in range(start-1, -1, -1):
                if A[i] == 'x':
                    ldist += start - i - count - 1
                    count += 1
                    
        #print "ldist: ", ldist
        rdist = 0
        if max_i != len(A):
            count = 0
            for i in range(max_i+1, len(A)):
                if A[i] == 'x':
                    rdist += i - max_i - count -1
                    count += 1
                    
        
        #print "rdist: ", rdist
        
        return (ldist + rdist) % 10000003

