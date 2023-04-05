for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    lst = [list(map(int,input().split())) for _ in range(M)]
    dist = [0] + [999] * N
    for _ in range(1):
        for f, t, d in lst:
            dist[t] = min(dist[f]+d,dist[t])
    print(f'#{test_case} {dist[-1]}')