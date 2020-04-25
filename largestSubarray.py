from collections import defaultdict
from sys import maxsize
def maxSubarray(A):
    max_so_far = -maxsize-1
    current_max_sum = 0
    start_index, end_index, final_start_inedx = 0, 0, 0
    for i in range(0, len(A)):
        current_max_sum += A[i]
        if max_so_far < current_max_sum:
            max_so_far = current_max_sum
            end_index = i                                   #current index
            final_start_inedx = start_index                 #store the start index in final
        if current_max_sum < 0:
            current_max_sum = 0
            start_index += 1
    return [max_so_far, final_start_inedx, end_index]



print(maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(maxSubarray([-1,-2,-3,-4,-5,-6]))