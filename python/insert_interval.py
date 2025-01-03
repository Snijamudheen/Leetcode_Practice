# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion. Note that you don't need to modify intervals in-place. You can make a new array and return it.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # if current interval after new interval, so first value of current should be more than second value of new interval 
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)  # so now append new 
                return res + intervals[i:]  # so new is before the rest of the intervals

            # if current interval is before the new interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) # so current interval is before new interval

            else: # if its overlapping, then merge by taking the min of both the intervals(first values) as the first value, and max for the second value
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res
