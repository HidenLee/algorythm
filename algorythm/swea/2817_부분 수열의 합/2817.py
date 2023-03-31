for _ in range(1,int(input())+1):
    N, K = map(int,input().split())
    lst = list(map(int,input().split()))
    vistied = [1]* N
    cnt = 0
    for i in range(1<<N):
        temp = 0
        for j in range(N):
            if temp <= K and i & (1<<j):
                temp += lst[j]
        if temp == K:
            cnt += 1
    print(f'#{_} {cnt}')