N, M = map(int,input().split())
arr = list(input().split())
arr.sort(key=(lambda x : ord(x)))
# for i in range(M-3):
#     for j in range(i+1,M-2):
#         for k in range(j+1,M-1):
#             for l in range(k+1,M):
#                 print(arr[i]+arr[j]+arr[k]+arr[l])

from itertools import combinations
for comb in combinations(arr,N):
    jcnt = 0
    mcnt = 0
    flag = True
    for elm in comb:
        if elm not in ["A","E","I","O","U","a","e","i","o","u"]:
            jcnt += 1
        else:
            mcnt += 1
        if jcnt >=2 and mcnt >=1:
            break
    else:
        flag = False
    if flag:
        print("".join(comb))
