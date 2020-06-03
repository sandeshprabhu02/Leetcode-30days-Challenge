"""

Move Zeroes
Solution
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""




class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        for i in range(n):
            print("i", nums[i])
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
            print("nums", nums)
        while count < n:
            nums[count] = 0
            count += 1
        return nums



nums = [9,0,9,0,9]
print(Solution().moveZeroes(nums))