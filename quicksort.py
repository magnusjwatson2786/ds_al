'''
QuickSort time complexity: O(n log n) [best case]
                           O(n^2) [worst case]
'''

def quicksort(arr):
    if len(arr)<=1:
        return arr

    ltpivot=[]
    gtpivot=[]
    pivot=arr[0]

    for i in arr[1:]:
        if i <= pivot:
            ltpivot.append(i)
        else:
            gtpivot.append(i)

    return quicksort(ltpivot) + [pivot] + quicksort(gtpivot)
