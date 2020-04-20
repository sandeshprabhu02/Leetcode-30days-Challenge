"""

Leetcode 253: Meeting Rooms II
Posted on July 26, 2018
Question
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
 find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]

"""


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def meetingRooms2(self, intervals):
        n = len(intervals)
        if not intervals:
            return 0
        if n == 1:
            return 1
        start, end = [], []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        min_rooms, count_rooms = 0, 0
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                count_rooms += 1
                min_rooms = max(min_rooms, count_rooms)
                s += 1
            else:
                count_rooms -= 1
                e += 1
        return min_rooms

        


# lst = []
# lst.append(Interval(0, 30))
# lst.append(Interval(5, 10))
# lst.append(Interval(15, 20))

print(Solution().meetingRooms2([[9,10], [4,9], [4,17]]))
# print(Solution().meetingRooms2([[0, 30],[5, 10],[15, 20]]))
# print(Solution().meetingRooms2([[7,10],[2,4]]))


