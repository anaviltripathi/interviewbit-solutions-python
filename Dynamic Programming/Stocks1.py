class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        mProfit = 0
        if len(A) < 2: return 0
        
        
        smallest = A[0]
        largest = A[1]
        
        mProfit = largest - smallest
        currProfit = mProfit
        
        for i in range(1,len(A)):
            if A[i] > largest:
                currProfit = currProfit + A[i] - largest
                largest = A[i]
            elif A[i] < smallest:
                smallest = A[i]
                largest = A[i]
                currProfit = 0
            
            mProfit = max(mProfit, currProfit)
            
        
        return mProfit
                
                

