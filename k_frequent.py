from distutils.command.build_scripts import first_line_re


# def k_frequent(arr,k):
    # first_dict = {}
    # freq_dict = {}
    # for i in arr:
    #     if i not in first_dict:
    #         first_dict[i] = 1
    #     else:
    #         first_dict[i] += 1

    # for key, value in first_dict.items():
    #     if value not in freq_dict:
    #         freq_dict[value] = [key]
    #     else:
    #         freq_dict[value].append(key)

    # print(first_dict)
    # print(freq_dict)
# import heapq

# def k_frequent(a,k):
#     heapq.heapify(a)
#     x = [[] for i in range(len(a))]
#     print(x)
#     for i in range(len(a)):
#         # print(a[i])
#         x[i].append(heapq.heappop(a))
#     print(x)
def k_frequent(a,k):
    count_map = {}
    for i in arr:
        count_map[i] = 1 + count_map.get(i,0)
    freq = [[] for i in range(len(arr)+1)]
    print(freq)
    for y,v in count_map.items():
        freq[v].append(y)
    print(freq)
    res = []
    for j in range(len(freq)-1,0,-1):
        for n in freq[j]:
            res.append(n)
            print(len(res))
            if len(res) == k:
                print(res)
                return res

arr =  [7, 7, 7, 7, 7 ]
k = 1

k_frequent(arr,k)
# Output:

# [3, 1]