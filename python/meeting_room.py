# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

'''Input:
[[0, 30], [5, 10], [15, 20]]

Sorted intervals:
After sorting by start times:
[[0, 30], [5, 10], [15, 20]]

Check overlaps:

Compare [5, 10] with [0, 30] → Overlap!
(Meeting 2 starts at 5 but Meeting 1 ends at 30)
Return False. '''

class Solution:
    """
    @param intervals: a list of meeting time intervals
    @return: True if the person can attend all meetings, False if not
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Sort the meetings by their start times
        # This way, we can check if any meeting overlaps with the next one
        intervals.sort(key=lambda interval: interval.start)       # lambda arguments: expression


        # Go through each meeting (starting from the second one)
        for i in range(len(intervals)-1): #The loop runs from i = 0 to i = len(intervals) - 2 to avoid going out of bounds
            # If a meeting starts before the previous one ends, there's an overlap
            if intervals[i].end > intervals[i + 1].start:
                return False  # The person can't attend all meetings

        # If no overlaps were found, the person can attend all meetings
        return True
