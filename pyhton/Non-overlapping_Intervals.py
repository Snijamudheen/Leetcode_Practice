# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()  #sort the list

        res = 0
        prevEnd = intervals[0][1] #end value(1) of the current/first interval(0)

        for start, end in intervals[1:]: # go thru all intervals starting at the second since first is already initialized above
            if start >= prevEnd:  #not overlapping case
                prevEnd = end
            else:  #overlapping
                res += 1  #update res/count
                prevEnd = min(end, prevEnd) # we wanna delete the interval with the least value of ending time
        
        return res
