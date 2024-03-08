#https://www.acmicpc.net/problem/12865 평범한배낭

# from collections import deque

N, K = map(int, input().split())
dp = [0 for _ in range(K+1)]
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
lst.sort(key= lambda x:(x[0]))

for w,v in lst:
    for idx in range(K,w-1,-1):
        dp[idx] = max(dp[idx],dp[idx-w]+v)
print(dp[K])

# W,V = X[0],X[1]

