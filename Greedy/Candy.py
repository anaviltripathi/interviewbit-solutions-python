class Solution:
    # @param ratings : list of integers
    # @return an integer
    def candy(self, ratings):
        if not ratings: return 0
        
        min_total_count = 1
        curr_count = 1
        last_i = -1
        last_count = 1
        
        
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                last_i = i-1
                curr_count += 1
                last_count = curr_count
                min_total_count += curr_count
                
            elif ratings[i] < ratings[i-1]:
                #curr_count = 1
                
                if last_count == 1:
                    last_count = 1
                    curr_count = 1
                    min_total_count += i - last_i
                elif last_count > 1:
                    last_count -= 1
                    curr_count = 1
                    min_total_count += i - last_i -1 
                else:
                    curr_count = 1
                    min_total_count += curr_count
            else:
                last_i = i-1
                last_count = 1
                curr_count = 1
                min_total_count += curr_count
                

            #print min_total_count, curr_count
                
        return min_total_count
                

