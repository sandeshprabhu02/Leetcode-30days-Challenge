"""

Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


"""


class Solution:
    def trap(self, arr):
        left = right = 0
        i, j = 0, len(arr)-1
        water = 0
        while i <= j:
            print(arr[i])
            print(arr[j])
            left = max(left, arr[i])
            right = max(right, arr[j])
            while i <= j and arr[i] <= left <= right:
                water += left - arr[i]
                i += 1
            while i <= j and arr[j] <= right <= left:
                water += right - arr[j]
                j -= 1
            print('left', left)
            print('right', right)
            print('water', water)
            print('-----')
        return water






# print(Solution().trap([2, 0, 2]))
# print(Solution().trap([3, 0, 0, 2, 0, 4]))
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))