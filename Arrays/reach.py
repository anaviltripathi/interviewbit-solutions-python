class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        minDist = 0
        if not X and not Y: return 0
        
        if len(X) == 1: return 0
        
        for i in range(1,len(X)):
            nearest_diagnol_end = min(abs(X[i] - X[i-1]), abs(Y[i] - Y[i-1]))
            minDist += nearest_diagnol_end + abs(abs(X[i] - X[i-1]) - nearest_diagnol_end) + abs(abs(Y[i] - Y[i-1]) - nearest_diagnol_end)
            
            
        return minDist

