class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, s1, s2, s3):
        '''
        if len(s1)+ len(s2) != len(s3): return 0
        elif s1 == '' or s2 == '': return s2==s3 or s1==s3
        else:
            Arr = [1 for i in range(len(s2)+1)]
            for i in range(1,len(s2)+1):
                Arr[i] = Arr[i-1] and s3[i-1] == s2[i-1]
            for i in range(1,len(s1)+1):    
                Arr[0] = Arr[0] and s3[i-1] == s1[i-1]
                for j in range(1,len(s2)+1):
                    Arr[j] = (Arr[j-1] and s3[i+j-1] == s2[j-1]) or (Arr[j] and s3[i+j-1]== s1[i-1])

        return Arr[-1]
        '''
        cache = {}
        
        
        def isInterleaveHelper(s1, s2, s3):
            if not s1 and not s2 and not s3:
                return True
            elif not s1:
                if s2 == s3:
                    return True
                else:
                    return False
            elif not s2:
                if s1 == s3:
                    return True
                else:
                    return False
            
            if (len(s1),len(s2),len(s3)) in cache:
                return cache[(len(s1),len(s2),len(s3))]
            
            cache[(len(s1),len(s2),len(s3))] = False
            if s1[0] == s3[0]:
                if isInterleaveHelper(s1[1:], s2, s3[1:]):
                    cache[(len(s1),len(s2),len(s3))] = True
                    return True
            
            if s2[0] == s3[0]:
                if isInterleaveHelper(s1, s2[1:], s3[1:]):
                    cache[(len(s1),len(s2),len(s3))] = True
                    return True
            
            return False
        
        return isInterleaveHelper(s1,s2,s3)

