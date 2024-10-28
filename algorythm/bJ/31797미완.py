# N,M = map(int,input().split())
# target = N % (M*2)
# apt = [0] * (target+1)
# for human in range(1,M+1):
#     for ipt in tuple(map(int,input().split())):
#         if ipt > target:
#             continue
#         apt[ipt] = human

# for idx in range(target):
#     if apt[idx]:
#         continue
#     apt[idx] = apt[idx-target]

# if apt in ipt:
#     print(human)