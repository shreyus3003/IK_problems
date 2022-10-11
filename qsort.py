import random
# def helper(a,start,end):
#     if start >= end:
#         return
#     rand_num  = random.randint(start, end)
#     # rand_num  = 0
#     print(a[rand_num])
#     a[rand_num], a[start] = a[start], a[rand_num]
#     pivot = a[start]
#     print(a)
#     smaller = start
#     for bigger in range(start+1, end+1):
#         print(a[bigger])
#         print(pivot)
#         if a[bigger] < pivot:
#             # print(smaller)
#             smaller += 1
#             print("bigger", a[bigger])
#             print("smaller", a[smaller])
#             a[smaller], a[bigger] = a[bigger], a[smaller]
#     print(smaller)
#     a[start], a[smaller] = a[smaller], a[start]


# def qsort(a):
#     helper(a, 0 , len(a)-1)
#     return 
    

def helper(a, start, end):
    if start >= end:
        return
    rand = random.randint(start, end)
    a[rand], a[start] = a[start], a[rand]
    pivot = a[start]
    smaller  = start
    for big in range(start+1, end+1):
        if a[big] < pivot:
            smaller += 1
            a[big], a[smaller] = a[smaller], a[big]
    a[start], a[smaller] = a[smaller], a[start]
    helper(a,start, smaller-1)
    helper(a, smaller+1, end)

def qsort(a):
    start = 0
    end = len(a)-1
    helper(a, start, end)

a = [6,3,7,8,9,2,4]
qsort(a)
print(a)