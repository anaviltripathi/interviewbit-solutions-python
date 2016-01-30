class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        lo = max(C)
        hi = sum(C)
        
        while lo < hi:
            mid = (lo + hi) / 2
            requiredPainters = getRequiredPainters(mid, C)
            if requiredPainters <= A:
                hi = mid
            else:
                lo = mid + 1
            #print mid , requiredPainters
        return lo*B % 10000003

def getRequiredPainters(mid, C):
    num = 1
    s = 0
    for i in C:
        s += i
        if s > mid:
            num += 1
            s = i
    return num
        

