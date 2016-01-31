class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        if len(A) < 4: return []
        A = sorted(A)
        #print A
        d = []
        i = 0
        while i < len(A) - 3:
            while i > 0 and i < len(A) - 3 and A[i] == A[i-1]:
                    i += 1
            j = i + 1
            
            while j < len(A)-2:
                while j > i + 1 and j < len(A)  and A[j] == A[j-1]:
                    j += 1
                
                if j >= len (A)- 2: break
            
                first_pair = A[i] + A[j]
                k = j + 1
                l = len(A) - 1
                while k < l:
                    while k > j + 1 and k < len(A) and A[k] == A[k-1]:
                        k += 1
                    
                    if k == len(A) or k == l: break
                
                    while l < len(A) - 1 and l > k+1 and A[l] == A[l+1]:
                        l -= 1
                    second_pair = A[k] + A[l]
                    value = second_pair + first_pair
                    if  value == B:
                        d.append([A[i], A[j], A[k], A[l]])
                        k += 1
                        l -= 1
                    elif value < B:
                        k += 1
                    else:
                        l -= 1
                j += 1
            i += 1
            
        return sorted(d)

