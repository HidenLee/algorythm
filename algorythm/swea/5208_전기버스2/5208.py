for _ in range(1,int(input())+1):
    N, *lst = list(map(int,input().split()))
    nowidx = 0
    cnt = 0
    ans = 999
    stack = [(nowidx,cnt)]
    while stack:
        nowidx, cnt = stack.pop()
        print(nowidx,cnt)
        if nowidx >= N-1:
            if  ans > cnt:
                ans = cnt
            continue
        if ans <= cnt:
            continue
        for i in range(1,lst[nowidx]+1):
            stack.append((nowidx+i,cnt+1))
    print(f'#{_} {ans-1}')