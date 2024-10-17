# https://www.acmicpc.net/problem/10026

N = int(input())
arr = [[1 if x =="R" else 0 if x == "B" else -1 for x in list(input()) ] for _ in range(N)]

visit = [[[False,False] for _ in range(N)]for _ in range(N)]

delta = [(1,0),(0,1),(-1,0),(0,-1)]

from collections import deque

def bfs(x,y,isSick):
    global visit
    deq = deque([(x,y)])
    while deq:
        ox, oy = deq.pop()
        # visit[ox][oy][1 if isSick else 0] = True

        for nx, ny in [(ox+dx,oy+dy) for dx,dy in delta]:
            if 0<=nx<N and 0<=ny<N :
                
                if isSick and not visit[nx][ny][1]:
                    if  arr[nx][ny] * arr[x][y] == -1 and not visit[nx][ny][1] or arr[nx][ny] == arr[x][y]:
                        visit[nx][ny][1] = True
                        deq.appendleft((nx,ny))
                if not isSick and arr[nx][ny] == arr[x][y] and not visit[nx][ny][0]:
                    visit[nx][ny][0] = True
                    deq.appendleft((nx,ny))


                # if arr[nx][ny] == arr[x][y] and not visit[nx][ny][0]:
                #     visit[nx][ny][0] = True
                #     visit[nx][ny][1] = True
                #     deq.appendleft((nx,ny,False))
                #     deq.appendleft((nx,ny,True))

                # if arr[nx][ny] * arr[x][y] == -1 and not visit[nx][ny][1] and isSick:
                #     visit[nx][ny][1] = True
                #     deq.appendleft((nx,ny,True))

# bfs(0,0)


cnt = [0,0]
for i in range(N):
    for j in range(N):
        if all(visit[i][j]):
            continue
        # bfs(i,j)
        if not visit[i][j][0] :
            bfs(i,j,False)
            cnt[0] += 1
            visit[i][j][0] = True
        if not visit[i][j][1] : 
            bfs(i,j,True)
            cnt[1] += 1   
            visit[i][j][1] = True
        # print()
        # for _ in range(N):
        #     print(visit[_])
    
print(*cnt)