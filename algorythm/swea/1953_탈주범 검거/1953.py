tunneldict = {0:[],1:[(0,1),(1,0),(0,-1),(-1,0)], 2:[(1,0),(-1,0)],3:[(0,1),(0,-1)],4:[(-1,0),(0,1)],5:[(1,0),(0,1)],6:[(0,-1),(1,0)],7:[(-1,0),(0,-1)]} 

def side(y,x,table):
    lst = [(y+dlt[0],x+dlt[1]) for dlt in tunneldict[table[y][x]] if 0 <= y+dlt[0] < N and 0 <= x+dlt[1] < M] 
    return lst

T = int(input())
for test_case in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(N)]
    queue= [(R,C,1)]
    visited = [[0]*M for _ in range(N)]
    while queue:
        y, x, dist = queue.pop(0)
        if dist <= L:
            visited[y][x] = 1    
            for nxty, nxtx in side(y,x,array):
                if not visited[nxty][nxtx] and (y,x) in side(nxty,nxtx,array):
                    queue.append((nxty,nxtx,dist+1))
    rst = sum(sum(visited,[]))
    print(f'#{test_case} {rst}')