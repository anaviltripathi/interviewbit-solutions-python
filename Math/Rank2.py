class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        l = sorted(list(A))
        rank = 1
        length = len(A)
        
        for i in range(len(A)):
            shifts = calc_permus(length - i -1, l, A[i])
            l.remove(A[i])
            for s in shifts:
                rank += s % 1000003
        
        return rank % 1000003

def calc_permus(n, l, a):
    
    #total permus
    f = 1
    for j in range(n):
        f *= (j + 1) % 1000003
    
    #preceding characters    
    i = 0
    while l[i] != a:
        i += 1
    
    list_of_preceding_chars = l[:i]
    other_list = l[i:]
    rs = findRepeatedCharacters(list_of_preceding_chars)
    other_rs = findRepeatedCharacters(other_list)
    for r in other_rs:
        for j in range(r):
            f /= (j+1)
    
    shifts = []
    for i in range(len(rs)):
        new_f = f
        for j in range(len(rs)):
            if i != j:
                for k in range(rs[j]):
                    new_f /= (k + 1) % 1000003
            else:
                for k in range(0, rs[j]-1):
                    new_f /= (k + 1) % 1000003
        shifts.append(new_f)
    
    return shifts



def findRepeatedCharacters(l):
    n = []
    from collections import Counter
    c = Counter(l)
    for i in c:
        #if c[i] > 1:
        n.append(c[i])
    return n


