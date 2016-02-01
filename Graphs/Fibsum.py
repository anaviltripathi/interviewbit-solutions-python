class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        fibs = [1, 1]
        while True:
            res = fibs[-1] + fibs[-2]
            if res > A:
                break
            else:
                fibs.append(res)
        count = 0
        i = 0
        while A > 0:
            num = fibs[~i]
            if A >= num:
                count += A/num
                A %= num
            i += 1
            
        return count

