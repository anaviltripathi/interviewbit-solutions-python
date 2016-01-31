class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        n = len(A)
        d = {}
        res = []
        for i in range(n-1):
            for j in range(i+1, n):
                s = A[i] + A[j]
                if s not in d:
                    d[s] = (i,j)
                else:
                    if d[s][0] == i or d[s][1] == j or d[s][1] == i or d[s][0] == j:
                        continue
                    else:
                        res.append(list(d[s]) + [i,j])
        
        return sorted(res)[0] if res else res
                    

