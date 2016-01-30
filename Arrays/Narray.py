class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        length = len(A)
        SigmaN = length*(length+1)/2
        SigmaNsquare = length * (length+1) * (2*length +1)/6
        AminusB = sum(A) - SigmaN
        square_sum = 0
        
        for i in range(len(A)):
            square_sum += A[i]*A[i]
            
        SquareMinus = square_sum - SigmaNsquare
        
        AplusB = SquareMinus/AminusB
        
        return [(AplusB+AminusB)/2, (AplusB-AminusB)/2]
        
        
      

