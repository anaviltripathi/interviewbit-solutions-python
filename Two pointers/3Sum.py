class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        #if len(A) < 3: return None
        A = sorted(A)
        n = len(A)
        import sys
        
        mindiff = sys.maxint
        
        for i in range(len(A)-2):
            j = i + 1
            k = n - 1
            while j < k:
                s = A[i] + A[k] + A[j]
                diff = abs(B - s)
                
                if diff == 0:
                    return s
                
                if diff < mindiff:
                    mindiff = diff
                    result = s
                
                if s <= B:
                    j += 1
                else:
                    k -= 1
         
        
        return result

