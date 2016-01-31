class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        array_one = "1"
        A = A-1


        for i in xrange(A):
            j = 0
            array_two = ""
            while j < len(array_one) - 1:
                count = 1
                while j+1 < len(array_one) and array_one[j] == array_one[j+1]:
                    j += 1
                    count += 1
                array_two = array_two + str(count)
                array_two = array_two + str(array_one[j])
                j += 1

            if len(array_one) == 1:
                array_one = "11"
            elif array_one[-1] != array_one[-2]:
                array_two= array_two + str(11)
                array_one = array_two[:]
            elif array_one[-1] == array_one[-2]:
                array_one = array_two


        return array_one


