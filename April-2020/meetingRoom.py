"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true

"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def meetingRooms(self, intervals):
        n = len(intervals)
        print(n)
        if n <= 1:
            return True
        intervals.sort(key=lambda x: x.start)
        #check the sorted intervals
        for x in intervals:
            print(x.start, x.end)
        for i in range(n-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True


# lst = []
# lst.append(Interval(0, 30))
# lst.append(Interval(5, 10))
# lst.append(Interval(15, 20))
# print(Solution().meetingRooms(lst))


lst2 = []
lst2.append(Interval(7, 10))
lst2.append(Interval(2, 4))
print(Solution().meetingRooms(lst2))