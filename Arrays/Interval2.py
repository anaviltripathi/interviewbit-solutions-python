# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        merged_interval = []
        
        for interval in sorted(intervals, key = lambda i: i.start):
            if merged_interval != [] and merged_interval[-1].end >= interval.start:
                merged_interval[-1].end = max(merged_interval[-1].end, interval.end)
            else:
                merged_interval += interval,
       
            
        return merged_interval
        
