class Solution:
    # @param dividend : integer
    # @param divisor : integer
    # @return an integer
    def divide(self, dividend, divisor):
        if dividend > 2147483647 or divisor == 0:
            return 2147483647
        
        if dividend == 0:
            return 0
        if dividend * divisor < 0:
            negative = True
        else:
            negative = False
            
        #count = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        #while dividend>=divisor:
        #    i = 1
        #    x = divisor
        #    while dividend >= x+x:
        #        i += i
        #        x += x
        #    
        #    dividend -= x
        #    count += i
        
        t = 0
        q = 0
        for i in range(32):
            if t + (divisor << i) <= dividend:
                t += (divisor << i)
                q |= 1<<i
                
        
        q = -q if negative else q
        return 2147483647 if q >= 2147483647 or q = -2147483648 else q
            

