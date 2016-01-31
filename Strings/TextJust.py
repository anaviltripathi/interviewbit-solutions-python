class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        words = A
        maxWidth = B
        if not A: return []
        
        if maxWidth == 0: return [""]
        
        para = []
        line = []
        line_length = 0
        no_of_words = 0
        
        for i in range(len(words)):
            
            if line_length + len(words[i]) <= maxWidth:
                line_length += (len(words[i]) + 1)
                line.append(words[i])
                no_of_words += 1
            
            else:
                line_length -= 1
                extra_spacing = maxWidth - line_length
                s = ""
                if no_of_words > 1:
                    extra_spacing_per_word = (maxWidth - line_length)/(no_of_words-1)
                    left_extra = (maxWidth - line_length) % (no_of_words-1)
                    j = 0
                    
                    for word in line[:-1]:
                        if left_extra:
                            k = 1
                            left_extra -= 1
                        else:
                            k = 0
                        j += 1
                        s += word + " "*(extra_spacing_per_word+1) + " "*k
                        
                else:
                    line[0] = line[0] + (maxWidth - len(line[0]))*" "
                s += line[-1]
                para.append(s)
                
                line = [words[i]]
                line_length = len(words[i]) + 1
                no_of_words = 1            
        
        words_covered = 0
        
        for line in para:
            words_covered += len(line.split())
            
        para = para + [' '.join(words[words_covered:])]
        para[-1] = para[-1] + " "*(maxWidth- len(para[-1]))
                
        return para

