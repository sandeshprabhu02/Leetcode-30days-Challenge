"""

Contiguous Array
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.


"""

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, count = 0, 0
        lookup = {0: -1}
        for i, num in enumerate(nums):
            print('lookup', lookup)
            count += 1 if num == 1 else -1
            if count in lookup:
                result = max(result, i - lookup[count])
            else:
                lookup[count] = i
            print('count', count)
            print('result', result)
            print('-------------')

        return result



print(Solution().findMaxLength([0, 1, 0, 1, 1, 1, 0]))