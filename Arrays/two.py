#Locate smallest window to be sorted 

""" Given an array of integers that are out of order, determine the bounds of the smallest 
window that must be sorted in order for the entire array to be sorted. For example, 
given [ 3 , 7 , 5 , 6 , 9] , you should return ( 1 , 3 )

"""

def window(array):
    left, right = None, None
    n = len(array)
    max_seen, min_seen = -float("inf"), float("inf")

    for i in range(n):
        max_seen = max(max_seen, array[i])
        if array[i] < max_seen:
            right = i
        
    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, array[i])
        if array[i] > min_seen:
            left = i

    return left, right


print(window([3, 7, 5, 6, 9]))