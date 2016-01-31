class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        from collections import Counter
        k = []
        if B > len(A): return []
        else:
            m = Counter(A[:B])
            k.append(len(m))
            #print k
            for i in range(1, len(A) - B+1):
                if m[A[i-1]] == 1: 
                    m.pop(A[i-1])
                    k.append(k[-1]-1)
                else:
                    m[A[i-1]] -= 1
                    k.append(k[-1])
                    
                if A[i+B-1] not in m:
                    m[A[i+B-1]] = 1
                    k[-1] += 1
                else:
                    m[A[i+B-1]] += 1
        
        return k
            

