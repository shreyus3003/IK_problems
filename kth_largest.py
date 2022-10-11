import heapq

# def kth_largest(a, k):
#     heapq.heapify(a)
#     x = heapq.nlargest(k,a)
#     print(min(x))
def helper(a, start, end, k):
    
    if start >= end:
        return 
    if len(a) < k:
        return 
    mid = start +(end-start)/2
    # print(a[int(mid)])
    mid = int(mid)
    a[start], a[mid] = a[mid], a[start]
    pivot = a[start]
    smaller = start
    for big in range(start+1, end+1):
        if a[big] < pivot:
            smaller += 1
            a[big], a[smaller] = a[smaller], a[big]
    a[smaller], a[start] = a[start], a[smaller]
    helper(a, start, smaller-1, k)
    helper(a, smaller+1, end, k)

def kth_largest(a, k):
    start = 0
    end = len(a)-1
    helper(a, start, end,k)
    n = len(a)
    res = a[n-k]
    print(res)

a =  [5, 1, 10, 3, 2]
k = 2
kth_largest(a, k)
print(a)