class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        #k = int(A)
        if len(A) == 1 and int(A) < 2: 
            return 0
        #while k > 1:
        #    if k % 2 == 1:
        #        return 0
        #    k /= 2
        
        res = []    
        carry = '0'
        while len(A) > 1 or int(A) > 1:
            if len(A) == 1:
                if int(A) == 2 or int(A) == 4 or int(A) == 8:
                    return 1
                else:
                    return 0
            for i in A:
                res.append(str(int(carry + i)/2))
                if int(carry + i) % 2 == 1:
                    carry = '1'
                else:
                    carry = '0'
            
            while res[0] == '0':
                res = res[1:]
            
            A = ''.join(res)
            #print A
            if int(A[-1]) % 2  == 1:
                return 0
                
            
            res = []
            
            
        return 1

