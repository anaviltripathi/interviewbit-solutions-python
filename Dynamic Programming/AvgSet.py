from collections import defaultdict

def ispossible(A,start,inset,target,cache):
    #print (start,inset,target)
    if inset == 0:
        if abs(target) < 1e-6:
            #print '\tSuccess'
            return True
        else:
            #print '\tOut of elem fail'
            return False
            
    if start == len(A):
        #print '\tEnd of list fail'
        return False
        
        
    key = (start,inset,target)
    if key in cache:
        return cache[key]
    sol = ispossible(A,start+1,inset-1,target - A[start],cache)\
        or ispossible(A,start+1,inset,target,cache)
    cache[key] = sol
    return sol
    
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def avgset(self, A):
        A = sorted(A)
        avg = float(sum(A)) / float(len(A))
        
        I = None
        Total = None
        for i in xrange(1, len(A)/2 + 1):
            if not ispossible(A,0,i,i*avg,{}):
                continue
            I = i
            Total = i*avg
            break
        if not I:
            return []
        
        cache = {}
        a = []
        b = []
        for j in xrange(len(A)):
            if ispossible(A,j+1,I-1,Total-A[j],cache):
                a.append(A[j])
                I -= 1
                Total -= A[j]
            else:
                assert(ispossible(A,j+1,I,Total,cache))
                b.append(A[j])
                    
        return [sorted(a),sorted(b)]

