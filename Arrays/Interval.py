# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        
        def overlaps(interval1, interval2):
            if interval1.start < interval2.start and interval1.end < interval2.start:
                return False
            if interval1.start > interval2.end and interval1.end > interval2.end:
                return False
                
            return True
        
        merged_intervals = []
        overlapped = False
        if not intervals:
            return [newInterval]
        elif newInterval.end < intervals[0].start:
            return [newInterval]+intervals
        elif newInterval.start > intervals[-1].end:
            return intervals+[newInterval]
        
        for i, interval in enumerate(intervals):
            if overlaps(interval, newInterval):
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)
                overlapped = True
            else:
                if not overlapped and newInterval.start > interval.end:
                    merged_intervals.append(interval)
                else:
                    break
                
        merged_intervals += newInterval,
        #print intervals[i].start
        if merged_intervals[-1].end < intervals[i].start:
            merged_intervals += intervals[i:]
        
        return merged_intervals
