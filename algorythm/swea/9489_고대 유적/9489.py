T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    digmap = [list(map(int,input().split())) for _ in range(N)]
    rst = 0
    for i in range(N):
        for j in range(M):
            if digmap[i][j] == 1:
                cnt = 0
                y = i
                while y < N and digmap[y][j]:
                    y += 1
                    cnt += 1
                if j+cnt < M and digmap[i][j+cnt]:
                    temp = digmap[i][j:]
                    if 0 in temp:
                        cnt = digmap[i][j:].index(0)
                    else:
                        cnt = len(temp)
                if rst < cnt:
                    rst = cnt
    print(f'#{test_case} {rst}')