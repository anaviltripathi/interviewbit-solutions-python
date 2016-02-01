class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        count = 0
        
        for i in range(len(A)):
            if count % 2== 0 and A[i] == 0:
                count += 1
            elif count % 2 == 0 and A[i] == 1:
                pass
            elif count % 2 == 1 and A[i] == 0:
                pass
            elif count % 2 == 1 and A[i] == 1:
                count += 1
            
        return count

