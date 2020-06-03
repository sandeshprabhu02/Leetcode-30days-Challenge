# K-th Largest Number
# Video explanation at https://www.youtube.com/watch?v=QGVCnjXmrNg
# Get 100+ more coding videos at http://coderpro.com/

"""
703. Kth Largest Element in a Stream
Easy

603

309

Add to List

Share
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note: 
You may assume that nums' length ≥ k-1 and k ≥ 1.

"""

class Solution(object):
  def findKthLargest(self, arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
      pivotIndex = self._partition(arr, left, right)
      if pivotIndex == len(arr) - k:
        return arr[pivotIndex]
      elif pivotIndex > len(arr) - k:
        right = pivotIndex - 1
      else:
        left = pivotIndex + 1
    return -1

  def _partition(self, arr, low, high):
    pivot = arr[high]
    index = low
    for j in range(low, high):
      if arr[j] <= pivot:
        arr[index], arr[j] = arr[j], arr[index]
        index += 1
    arr[index], arr[high] = arr[high], arr[index]
    return index


print(Solution().findKthLargest([5, 7, 2, 3, 4, 1, 6], 3))
# 5
