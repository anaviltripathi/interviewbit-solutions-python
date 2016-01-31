class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        curr_indent = ""
        res = []
        curr = ""
        for i,c in enumerate(A):
            if c == "[" or c == "{":
                if curr: res.append(curr_indent + curr)
                curr = curr_indent + c
                res.append(curr)
                curr_indent += "\t"
                curr = ""
            elif c == "]" or c == "}":
                if curr: res.append(curr_indent + curr)
                curr_indent = curr_indent[:-1]
                curr = curr_indent + c
                res.append(curr)
                curr = ""
            elif c == " ":
                curr = ""
            elif c == ",":
                if A[i-1] == "}" or A[i-1] == "]":
                    res[-1] = res[-1] + c
                else:
                    curr = curr_indent + curr + c
                    res.append(curr)
                    curr = ""
            else:
                curr += c

        return res

