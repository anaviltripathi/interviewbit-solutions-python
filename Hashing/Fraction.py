class Solution:
    # @param numerator : integer
    # @param denominator : integer
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return "NaN"
            
        if numerator * denominator < 0:
            neg = True
        else:
            neg = False
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        s = str(numerator/denominator)
        
        remainder = numerator%denominator
        
        if remainder:
            s += '.'
        
        d = {}
        
        #d[remainder] = len(s)
        
        i = len(s)
        while remainder:
            numerator = remainder * 10
            digit = str(numerator/denominator)
            
            if remainder in d:
                s = s[:d[remainder]]+ "(" + s[d[remainder]:] + ")"
                break
            else:
                s += digit
                d[remainder] = i
            
            remainder = numerator%denominator
            i += 1
        
        return s if not neg else "-"+s

