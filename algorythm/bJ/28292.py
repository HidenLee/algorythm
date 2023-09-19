# https://www.acmicpc.net/problem/28292
# 개미수열

"""
1
11
12
1121
122111
112213
12221131
1123123111
12213111213113
11221131132111311231
12221231123121133112213111
1123112131122131112112321222113113
1221311221113112221131132112213121112312311231


"""


def generate_nxtsequence(S):
    S += '0'
    comp = ['',0] # [s,cnt]
    nxtS = ''
    mx = 0
    for s in S:
        if s != comp[0]:
            if mx < int(s):
                mx = int(s)
            if comp[0]:
                nxtS += comp[0] + str(comp[1])
            comp[0] = s
            comp[1] = 1
        else:
            comp[1] += 1
    return nxtS, mx
            

T = int(input())
nxt = '1'
mx = 0
for i in range(T-1):
    nxt, temp = generate_nxtsequence(nxt)
    if mx < temp:
        mx = temp
print(nxt)
print(mx,len(nxt))
