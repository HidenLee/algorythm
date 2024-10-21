
def dfs(start_node):
    global table
    if table[start_node[1]][start_node[0]] == 0:
        return 0
    stack = [start_node]
    while stack:
        ox, oy = stack.pop()
        table[oy][ox] = 0
        for nx, ny in [(ox+dt[0],oy+dt[1]) for dt in [(0,1),(1,0),(0,-1),(-1,0)]]:
            if 0<=nx< M and 0 <=ny < N and table[ny][nx] == 1:
                stack.append((nx,ny))        
    return 1


for tc in range(1,int(input())+1):
    M, N, K = map(int,input().split())
    table = [[0 for _ in range(M)] for _ in range(N)]
    cabages = []
    cnt = 0
    for _ in range(K):
        x, y = map(int,input().split())
        cabages.append((x,y))
        table[y][x] = 1
    for cabage in cabages:
        cnt += dfs(cabage)
    print(cnt)     
