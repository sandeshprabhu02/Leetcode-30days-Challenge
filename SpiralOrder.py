"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""
class Solution:
    def spiralOrder(self, arr):
        totalRow = len(arr)
        totalCol = len(arr[0])
        curRow, curCol = 0, 0
        while curRow<totalRow and curCol<totalCol:
            for i in range(curCol, totalCol):
                print(arr[curRow][i], end=" ")
            curRow += 1
            
            for i in range(curRow, totalRow):
                print(arr[i][totalCol-1], end=" ")
            totalCol -= 1
            
            if curRow<totalRow:
                for i in range(totalCol-1, curCol-1, -1):
                    print(arr[totalRow-1][i], end=" ")
                totalRow -= 1
            
            if curCol < totalCol:
                for i in range(totalRow-1, curRow-1, -1):
                    print(arr[i][curCol], end=" ")
                curCol += 1
            
    

Solution().spiralOrder([[ 1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])