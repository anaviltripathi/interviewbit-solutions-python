# Code is correct but Interviewbit Judge has some problem
# in case of this problem

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        if A == None: return A
        d = {}
        list_of_groups = []
        group_number = 0
        for i in xrange(len(A)):
            sorted_A_i = ''.join(sorted(A[i]))
            if sorted_A_i not in d:
                list_of_groups.append([i+1])
                d[sorted_A_i] = group_number
                group_number += 1
            else:
                list_of_groups[d[sorted_A_i]].append(i+1)
        
        return  list_of_groups
        
    

