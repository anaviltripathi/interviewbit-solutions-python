class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        s = A
        if len(s) < 4 or len(s) > 12:
            return []
        
        return sorted(restoreHelper(s, 3))

def restoreHelper(s, dots):
    
    l = []
    #print "s: ", s, "dots: ", dots
    
    if dots == 0 and int(s) <= 255:
        if len(s) == 1:
            return [s]
        else:
            if int(s[0]) == 0:
                return []
        return [s]
    
    if int(s[0]) == 0:
        if isValid(s[1:], dots-1):
            for ip in restoreHelper(s[1:], dots-1):
                full_ip = s[0] + "." + ip
                l.append(full_ip)
        return l
        
    for i in range(3):
        if int(s[:i+1]) <= 255 and isValid(s[i+1:], dots-1):
            for ip in restoreHelper(s[i+1:], dots-1):
                full_ip = s[:i+1] + "." + ip
                #print full_ip
                l.append(full_ip)
    return l

def isValid(s, dots):
    if len(s) <= dots:
        return False
    if len(s) > (dots + 1) * 3:
        return False
    
    return True

