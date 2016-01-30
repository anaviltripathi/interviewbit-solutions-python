class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        count1, count2 ,poss1, poss2 = 0, 0 , 0,  1
        for n in A:
            if poss1 == n:
                count1 += 1
            elif poss2 == n:
                count2 += 1
            elif count1 == 0:
                count1, poss1 = 1, n
            elif count2 == 0:
                count2, poss2 = 1, n
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        
        for n in A:
            if n == poss1:
                count1 += 1
            elif n == poss2:
                count2 += 1
        #res = []
        
        if count1 > len(A)//3: return poss1
        if count2 > len(A)//3: return poss2
        return -1

