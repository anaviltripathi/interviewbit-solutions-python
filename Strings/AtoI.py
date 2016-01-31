class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        n = len(A)
        
        for i in range(n):
            if A[0] == ' ':
                A = A[1:]
            else:
                break
        
        num = 0
        pos = True
        for i in range(len(A)):
            if i == 0 and A[i] == '+' :
                pos = True
            elif i == 0 and A[i] == '-':
                pos = False
            elif not ('0' <= A[i] <= '9'):
                return num if pos == True else (-1)*num
            else:
                num = (num) * 10 + int(A[i])
                if num > 2147483647 and pos == True:
                    return 2147483647
                elif num > 2147483647 and pos == False:
                    return -2147483648
                    
        return num if pos == True else (-1) * num       
                    

