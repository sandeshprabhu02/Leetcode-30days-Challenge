# Enter your code here. Read input from STDIN. Print output to STDOUT

class Solution:
    def calculateArea(self, rect):
        height = int(rect[3]) - int(rect[1])
        width = int(rect[2]) - int(rect[0])
        return height * width

    def isRectangleOverlap(self, rect1, rect2):
        left = min(int(rect1[0]), int(rect2[0]))
        right = max(int(rect1[2]), int(rect2[2]))
        top = min(int(rect1[1]), int(rect2[1]))
        bottom = max(int(rect1[3]), int(rect2[3]))
        if left < right and top > bottom:
            return True
        else:
            return False

    def calculateAreaOfUncoilingRectangles(self, rect1, rect2):
        if not rect1 and not rect2:
            return 0
        if not rect1:
            return self.calculateArea(rect2)
        if not rect2:
            return self.calculateArea(rect1)
        if self.isRectangleOverlap(rect1, rect2):
            finalHeight = max(int(rect1[0]), int(rect1[2]), int(rect2[0]), int(rect2[2])) - min(int(rect1[0]), int(rect1[2]), int(rect2[0]), int(rect2[2]))
            finalWidth = max(int(rect1[1]), int(rect1[3]), int(rect2[1]), int(rect2[3])) - min(int(rect1[1]), int(rect1[3]), int(rect2[1]), int(rect2[3]))
            return finalHeight * finalWidth
        else:
            return 0

if __name__ == "__main__":
    # rect1 = str(input())
    # rect2 = str(input())
    # rect1 = rect1.split(' ')
    # rect2 = rect2.split(' ')
    print(Solution().calculateAreaOfUncoilingRectangles(['1', '1', '5', '5'], ['2', '2', '5', '5']))