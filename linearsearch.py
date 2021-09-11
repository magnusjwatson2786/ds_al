'''
Linear search
Time Complexity = O(n)
'''
def linearsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1