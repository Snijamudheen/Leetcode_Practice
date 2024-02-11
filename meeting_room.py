# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lamda i : i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True
