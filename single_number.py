"""

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

"""

class Solution(object):
    def singleNumber(self, nums):
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i] #use XOR operation
        return result

if __name__ == '__main__':
    nums = [2, 5, 2, 5, 8]
    print(Solution().singleNumber(nums))