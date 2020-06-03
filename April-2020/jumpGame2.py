"""
45. Jump Game II
Hard

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

"""

class Solution:
    def jump(self, nums):
        # jumps = currentIndex = nextIndex = 0
        # n = len(nums) - 1
        # while nextIndex < n:
        #     jumps += 1
        #     currentIndex, nextIndex = currentIndex, max(i + nums[i] for i in range(currentIndex, nextIndex + 1))
        # return jumps
        
        # n = len(nums)
        # if n < 2: return 0
        # level = currentMax = index = 0
        # while index <= currentMax:
        #     furthest = currentMax
        #     for i in range(1, currentMax):
        #         furthest = max(furthest, i + nums[i])
        #         if furthest >= n-1:
        #             return level + 1
        #     level += 1
        #     currentMax = furthest
        # return -1
        
        n = len(nums)
        result = nextMax = currentMax = 0
        for index in range(n-1):
            currentMax = max(currentMax, nums[index] + index)
            if index == nextMax:
                nextMax = currentMax
                result += 1
        return result



a = [1] * 10
print(Solution().jump([2,3,1,1,4]))
print(Solution().jump(a))