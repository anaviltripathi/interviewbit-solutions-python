class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        if not A:
            return 0
        elif len(A) == 1:
            return True if A == 'T' else False
            
        symbols = "".join([A[i] for i in range(len(A)) if (A[i] == "T" or A[i] == "F")])
        operators = "".join([A[i] for i in range(len(A)) if (A[i] != "T" and A[i] != "F")])
        
        n = len(symbols)
        #print len(symbols) - len(operators)
        #print symbols, operators
        T = [[0]*n for i in range(n)]
        F = [[0]*n for i in range(n)]
        for i in range(n):
            T[i][i] = 1 if symbols[i] == "T" else 0
            F[i][i] = 1 if symbols[i] == "F" else 0
            
        for gap in range(1, n):
            i = -1
            for j  in range(gap,n):
                i += 1
                for g in range(gap):
                    k = i + g
                    tot_ik = T[i][k] + F[i][k]
                    tot_kj = T[k+1][j] + F[k+1][j]
                    if operators[k] == "&":
                        T[i][j] += T[i][k] * T[k+1][j]
                        F[i][j] += (tot_ik * tot_kj - T[i][k] * T[k+1][j])
                    if operators[k] == "|":
                        T[i][j] += (tot_ik * tot_kj - F[i][k] * F[k+1][j])
                        F[i][j] += F[i][k] * F[k+1][j]
                    if operators[k] == "^":
                        T[i][j] += (T[i][k] * F[k+1][j] + F[i][k]*T[k+1][j])
                        F[i][j] += (T[i][k] * T[k+1][j] + F[i][k]*F[k+1][j])
                #print T[i][j]
        
        return T[0][-1]%1003
        
