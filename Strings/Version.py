class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        v1 = A.split('.')
        v2 = B.split('.')
        
        i = 0
        
        while i < len(v1) and i < len(v2):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            i += 1
        
        if len(v1) == len(v2): 
            return 0
        elif len(v1) > len(v2):
            while i < len(v1) and int(v1[i]) == 0:
                i += 1
            if i == len(v1):
                return 0
            else:
                return 1
        else:
            while i < len(v2) and int(v2[i]) == 0:
                i += 1
            if i == len(v2):
                return 0
            else:
                return -1

