class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        '''
        count = 0
        i = 0
        state = 0
        while i < len(A):
            if state == 0:
                if i == 0 or A[i] != A[count-1]:
                    A[count] = A[i]
                    state = 0
                    count += 1
                elif A[i] == A[count-1]:
                    A[count] = A[i]
                    state = 1
                    count += 1
            else:
                if A[i] != A[count-1]:
                    A[count] = A[i]
                    count += 1
                    state = 0
            
            i += 1
                    
             
        return count
        '''
        if not A:
            return 0
        count = 0
        i = 1
        j = 0 
        while i < len(A) and j < len(A):
            if i <= 1 or A[i] != A[j] or A[i] != A[j-1]:
                j += 1
                A[j] = A[i]
            i += 1
                
        
        return j + 1

