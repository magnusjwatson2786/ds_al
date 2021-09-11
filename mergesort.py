'''
Split takes time O(k log n)
Merge takes time O(n)
Overall time complexity = O(kn log n)
Space complexity = O(n)
'''

def mergesort(arr):
    if len(arr)<=1:
        return arr
    
    lh,rh=split(arr)
    left=mergesort(lh)
    right=mergesort(rh)
    print(left,right) 
    return merge(left,right)

def split(arr):
    mid=len(arr)//2
    lh=arr[:mid]
    rh=arr[mid:]
    return lh,rh

def merge(lh,rh):
    res=[]
    i=0
    j=0
    while i<len(lh) and j<len(rh):
        if lh[i]<rh[j]:
            res.append(lh[i])
            i+=1
        else:
            res.append(rh[j])
            j+=1
    while i<len(lh):
        res.append(lh[i])
        i+=1
    while j<len(rh):
        res.append(rh[j])
        j+=1
    return res

def verify_sorted(arr):
    n=len(arr)
    if n in [0,1]:
        return True
    return arr[0]<=arr[1] and verify_sorted(arr[1:])

alist=[43,21,32,54,65,76,98,78,89,21,12,23]
print(verify_sorted(alist))
# print(mergesort(alist))
print(verify_sorted(mergesort(alist)))