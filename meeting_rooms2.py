# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res,count = 0,0 #result which is the max meeting, count is the number of meeting ongoing
        s,e = 0,0 # s is the start position in the array and e is the end position

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else
                e -= 1
                count -= 1
            res = max(res, count) 
        return res
