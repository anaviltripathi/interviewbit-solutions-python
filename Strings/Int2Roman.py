class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        roman = ""
        if A >= 1000:
            roman = "M"*(A/1000)
            A = A%1000
        if A >= 900 and A < 1000:
            roman += "CM"
            A -= 900
        if A >= 500 and A < 900:
            roman += "D"
            A -= 500
        if A >= 400 and A < 500:
            roman += "CD"
            A -= 400
        if A >= 100 and A < 400:
            roman += "C"*(A/100)
            A = A % 100
        if A >= 90 and A < 100:
            roman += "XC"
            A -= 90
        if A >= 50 and A < 90:
            roman += "L"
            A -= 50
        if A >= 40 and A < 50:
            roman += "XL"
            A -= 40
        if A >= 10 and A < 40:
            roman += "X"*(A/10)
            A = A % 10
        if A == 9:
            roman += "IX"
            A -= 9
        if A >= 5 and A < 9:
            roman += "V"
            A -= 5
        if A == 4:
            roman += "IV"
        if A >= 1 and A < 4:
            roman += "I"*(A)
            
            
            
        return roman
            

