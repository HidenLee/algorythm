T = int(input())
for test_case in range(1,T+1):
    array = []
    N, M = list(map(int,input().split()))
    array = [list(map(int, input().split())) for _ in range(N)]
    delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    rst = []
    for i in range(N):
        for j in range(M):
            cnt = 0
            for dlt in delta: # 각 점에서 주변 방향 탐색
                if 0 <= i+dlt[0] < N and 0 <= j+dlt[1] < M: # 인덱스 아웃 방지
                    if array[i][j] > array[i+dlt[0]][j+dlt[1]]: # 봉우리 아님
                        cnt += 1
            if cnt >= 4:
                rst.append((i,j))
    print(f'#{test_case} {len(rst)}')
