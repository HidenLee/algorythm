T = int(input())
for test_case in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(N)]
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    tunneldict = {1:[(0,1),(1,0),(0,-1),(-1,0)], 2:[(1,0),(-1,0)]}
    queue= [(R,C)]
    visited = [[0]*M for _ in range(N)]
    while queue:
        y, x = queue.pop(0)
        visited[y][x] = 1    
        for dlt in tunneldict[array[y][x]]:
            if 0 <= y+dlt[0] < N and 0 <= x+dlt[1] < M and not visited[y+dlt[0]][x+dlt[1]]:
                if abs(y+dlt[0]-R) + abs(x+dlt[1]-C) < L:
                    queue.append((y+dlt[0],x+dlt[1]))
    