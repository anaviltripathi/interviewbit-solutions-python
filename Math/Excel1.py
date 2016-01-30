class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        #A = A[::]
        num = 0
        count = 0
        for i in range(len(A)-1,-1,-1):
            num += (ord(A[i]) - ord('A') + 1) * pow(26, count)
            count += 1
        return num
