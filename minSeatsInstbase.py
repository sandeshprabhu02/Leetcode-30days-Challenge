
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minSeatsAtInstabaseParty(self, empIntervals):
        n = len(empIntervals)
        if not empIntervals:
            return 0
        if n == 1:
            return 1
        start, end = [], []
        for i in empIntervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        min_seats, count_seats = 0, 0
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                count_seats += 1
                min_seats = max(min_seats, count_seats)
                s += 1
            else:
                count_seats -= 1
                e += 1
        return min_seats


if __name__ == "__main__":
    # N = input()
    # empIntervals = []
    # for i in range(N):
    #     temp = []
    #     inTime=  input()
    #     outTime = input()
    #     temp.append(inTime)
    #     temp.append(outTime)
    #     empIntervals.append(temp)
        print(Solution().minSeatsAtInstabaseParty([[9,10], [4,9], [4,17]]))