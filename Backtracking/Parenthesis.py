class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        paren_lis = self.helperParenthesis(A, 0, 0)
        return paren_lis
        
        
    
    def helperParenthesis(self, A, left_count , right_count):
        paren_lis = []
        
        if A == left_count: 
            st = ""
            while right_count < left_count:
                right_count += 1
                st = st + ")"
            return [st]
        #elif A = left_count and left_count == right_count: return [""]
        elif left_count > right_count :
            for st in self.helperParenthesis(A, left_count + 1, right_count):
                paren_lis.append( "(" + st )
            for st in self.helperParenthesis(A, left_count, right_count + 1):
                paren_lis.append( ")" + st)
            return paren_lis
            
        elif left_count == right_count: 
            for st in self.helperParenthesis(A, left_count + 1, right_count):
                paren_lis.append( "(" + st  )
        
            return paren_lis
            

