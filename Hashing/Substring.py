class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        import collections
        need, missing = collections.Counter(B), len(B)
        total_length = 0
        for s in B:
            total_length += len(s)
        
        #print need, total_length, missing
        start_list = []
        
        for i in range(len(A)- total_length + 1):
            start = i
            word_start = i
            j = i+1
            need, missing = collections.Counter(B), len(B)
            found = False
            while j < i + total_length + 1:
                if A[word_start:j] in need and need[A[word_start:j]] > 0:
                    #print start, A[word_start:j]
                    need[A[word_start:j]] -= 1
                    missing -= 1
                    if missing == 0:
                        #print A[word_start:j]
                        start_list.append(start)
                        break
                    if need[A[word_start:j]] < 0:
                        break
                    word_start = j
                    #print word_start
                    
                    
                j += 1
                    
        
        return start_list
        

