class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if m > n:
            n,m = m,n
            A,B = B,A
        if m == 0:
            if n == 0:
                return 0
            if n%2:
                return B[n/2]
            else:
                return (B[n/2]+B[n/2-1])/2.0
        low = 0
        high = m
        while low <= high:
            i = (low+high)/2
            j = (m+n+1)/2-i
            if (j == 0 or i == m or B[j - 1] <= A[i]) and (i == 0 or j == n or A[i-1] <= B[j]):
                if (m+n)%2:
                    if i == 0:
                        return B[j-1]
                    elif j == 0:
                        return A[i-1]
                    return max(A[i-1],B[j-1])
                else:
                    if i == 0:
                        return (B[j-1] + min(A[i],B[j]))/2.0
                    if j == 0:
                    	return (A[i-1] + min(A[i],B[j]))/2.0
                    if i == m:
                    	return (max(A[i-1],B[j-1]) + B[j])/2.0
                    if j == n:
                    	return (max(A[i-1],B[j-1]) + A[i])/2.0
                    return (max(A[i-1],B[j-1]) + min(A[i],B[j]))/2.0
            elif (j == 0 or i == m or B[j - 1] > A[i]):
                low = i+1
            elif (i == 0 or j == n or A[i-1] > B[j]):
                high = i-1
        return -1
        

