class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A = sorted(A)
        
        if A[-1] < 0:
            return A[-1] * A[-2] * A[-3]
        else:
            third_number = A[-1]
            other_two_mult = max((A[0]* A[1]), (A[-2]* A[-3]))
            return third_number * other_two_mult

