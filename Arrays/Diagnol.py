class Solution:
	# @param a : list of list of integers
	# @return a list of list of integers
	def diagonal(self, a):
	    B = [[] for i in range(len(a)*2)]
	    for i in range(len(a)):
	        for j in range(len(a)):
	            B[i+j].append(a[i][j])
	    
	    return B[:-1]
	   

