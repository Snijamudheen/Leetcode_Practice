# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0]) # i[0] cuz we sorting by the first value of the element
        output = [intervals[0]] #initialize the output of the merged intervals

        #iterate thru sorted intervals, skipped first intervals since it is already initialized above intervals[0]
        for start, end in intervals[1:]: 
            lastEnd = output[-1][1] #last/second value of the end intervals

            # overlapping, then merge. Checks if the start of the current interval is less than or equal to the end of the last  interval in the output list. If true, this indicates an overlap.
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end) # If there's an overlap, merge the current interval with the last interval in the output by updating the end of the last interval to the maximum of the current interval's end and the last interval's end. 
            else:
                output.append([start, end]) # If the current interval does not overlap with the last interval in the output list, it is added to the output list as a new interval.
        
        return output
