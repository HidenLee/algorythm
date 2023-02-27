delta = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    table = [[0]*N for _ in range(N)]
    table[N//2-1][N//2-1] = 2
    table[N//2][N//2] = 2
    table[N//2][N//2-1] = 1
    table[N//2-1][N//2] = 1
    for _ in range(M):
        y, x, c = map(int, input().split())
        y = y - 1
        x = x - 1
        table[y][x] = c
        for dlt in delta:
            stack = []
            ny, nx = y+dlt[0], x+dlt[1]
            while 0 <= ny < N and 0 <= nx < N: 
                if table[ny][nx] != c:
                    stack.append((ny,nx))
                    ny += dlt[0]
                    nx += dlt[1]
                else:
                    while stack:
                        ny,nx = stack.pop()
                        table[ny][nx] = c
                    break
    black = white = 0            
    for elm in sum(table,[]):
        if elm == 1:
            black += 1
        if elm == 2:
            white += 1
    print(f'#{test_case} {black} {white}')