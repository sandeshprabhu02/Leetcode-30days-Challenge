"""
Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""


class Solution:
    def search(self, nums, target):
        left, mid = 0, 0
        right = len(nums) -1
        while left <= right:
            mid = (left+right)//2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target >= nums[mid] and target < nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            print('-----')
        return -1



print(Solution().search([4,5,6,7,0,1,2], 0))
#4
print(Solution().search([4,5,6,7,0,1,2], 3))
#-1