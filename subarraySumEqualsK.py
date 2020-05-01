"""

560. Subarray Sum Equals K
Medium

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
Note:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


"""

class Solution:
    def subarraySum(self, nums, k):
        sums = {0:1}
        result, currentSum = 0, 0
        for n in nums:
            currentSum += n
            result += sums.get(currentSum - k, 0)
            sums[currentSum] = sums.get(currentSum, 0) + 1
        return result



print(Solution().subarraySum([1,1,1], 2))