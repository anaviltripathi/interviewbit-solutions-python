class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, digits):
        if not digits:
            return []
            
        #print digits
        
        phone = {1: ["1"], 2: ["a", "b", "c"], 3: ["d","e","f"], 4: ["g","h","i"], 5:["j","k","l"], 6: ["m","n","o"], 7: ["p","q","r","s"], 8: ["t","u","v"], 9: ["w","x","y","z"], 0: ["0"]}
        
        all_combs = []
        for letter in phone[int(digits[0])]:
            for comb in self.letterCombinations(digits[1:]) or [""]:
                all_combs.append(letter+comb)
        return all_combs

