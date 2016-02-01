class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        def nextNums(val):
            n = []
            if val - 1 >= 0:
                n.append(val-1)
            if val + 1 <= 9:
                n.append(val+1)
            return n
        graph = [i for i in range(10)]
        level = set(graph)
        res = set()
        while level:
            new_level = set()
            for num in level:
                if A <= num <= B:
                    res.add(num)
                val = num % 10
                for n in nextNums(val):
                    new_num = num*10 + n
                    if new_num <= B:
                        new_level.add(new_num)
            level = new_level
    
        return sorted(list(res))

