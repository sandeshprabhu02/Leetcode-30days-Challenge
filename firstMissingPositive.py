
#[6, 3, 4, -1, 1]
def firstMissingPositive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0: nums[i] = len(nums)+1
        for i in range(n):
            x = abs(nums[i])
            if x <= n:
                index = x-1
                y = -abs(nums[index])
                nums[index] = y
        for i in range(n):
            if nums[i] > 0: return i+1
        return n+1


arr = [-1, -2, 6, 2, 4, 5, 3]
print(firstMissingPositive(arr))