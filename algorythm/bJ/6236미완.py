def sol(K):
    cnt = 0
    var = 0
    for i in range(N):
        if cnt > ans:
            return False
        if arr[i] > K:
            return False
        if var + arr[i] >= K:
            cnt += 1
            var = K - arr[i]
    return True



N, M = map(int,input().split())
arr = []
ans = 10e9
for _ in range(N):
    arr.append(int(_))
