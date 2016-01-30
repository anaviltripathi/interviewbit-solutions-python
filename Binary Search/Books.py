class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        lo = max(A)
        hi = sum(A)
        
        if B > len(A): return -1
        
        while lo < hi:
            mid = (lo + hi) / 2
            requiredStudents = getRequiredStudents(mid, A)
            if requiredStudents <= B:
                hi = mid
            else:
                lo = mid + 1
        return lo

def getRequiredStudents(mid, C):
    num = 1
    s = 0
    for i in C:
        s += i
        if s > mid:
            num += 1
            s = i
    return num

