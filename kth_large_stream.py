# Given an initial list along with another list of numbers to be appended with the initial list and an 
# integer k, return an array consisting of the k-th largest element after adding each element from the first list to the second list.
import heapq
from multiprocessing import heap

# def kth_largest(k, a, b):
#     result= []
    
#     heapq._heapify_max(a)
#     # heapq._heapify_max(a)
#     for i in b:
#         temp = a
#         # print(temp)
#         heapq.heappush(temp, i)
#         x =heapq.nlargest(k,temp)
#         result.append(min(x))

#     print("result", result)

# def kth_largest(k, a, b):
#     res = []
#     for elem in b:
#         # elem = b[2]
#         aux = []

#         low = 0
#         for i in a: 
#             if elem < i and low == 0:
#                 aux.append(elem)
#                 low = 1
#             aux.append(i)
#         if elem >= a[len(a)-1]:
#             aux.append(elem)
#         a = aux
#         n = len(a)
#         res.append(a[n-k])
#         print(res)

def kth_largest(k, a, b):
    heapq.heapify(a)
    print(a)
    res = []
    for i in b:
        heapq.heappush(a,i)
        print(a)
        x = heapq.nlargest(k,a)
        res.append(min(x))
    print(res)



k = 3
a =  [3, 2, 1] #[4, 6],
b =   [4, 4, 4] #[5, 2, 20],
# output =[2, 3, 4]
""""k": 3,
"initial_stream": [4, 5, 6, 7],
"append_stream": [5, 6, 4]
[5, 6, 6]"""
kth_largest(k, a, b)