class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) < 2:
            return False
            
        i = 0
        j = 1

        while i < len(A) and j < len(A):
            if A[j] - A[i] < B:
                j += 1
            elif A[j] - A[i] > B:
                i += 1
            else:
                if j!= i:
                    return True
                else:
                    j += 1
        
        return False

