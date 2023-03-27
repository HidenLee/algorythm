from collections import deque
delta = [(0,0,1),(0,0,-1),(0,-1,0),(0,1,0),(1,0,0),(-1,0,0)]
import sys
sys.stdin = open('./input.txt','r')

M, N, H = map(int,input().split())
array = [[] for _ in range(H)]
tomatoes = []
for h in range(H):
    for j in range(N):
        temp = list(map(int,input().split()))
        for i in range(M):
            if temp[i] == 1:
                tomatoes.append((i,j,h))
        array[h].append(temp)
distance = [[[999]*M for _ in range(N)] for _ in range(H)]
for i,j,h in tomatoes:
    distance[h][j][i] = 0
    visited = set((i,j,h))
    nxts = deque([(i,j,h)])
    while nxts:
        i,j,h = nxts.popleft()
        validateroute = False
        for dlt in delta:
            ni,nj,nh = i+dlt[0],j+dlt[1],h+dlt[2]
            if 0<=ni<M and 0<=nj<N and 0<=nh<H and not array[nh][nj][ni] and not (ni,nj,nh) in visited:
                visited.add((ni,nj,nh))
                nxts.append((ni,nj,nh))
                if distance[nh][nj][ni] > distance[h][j][i]:
                    distance[nh][nj][ni] = distance[h][j][i] + 1
                    validateroute =True
        if not validateroute:
            nxts.clear()

rst = 0                 

for i,j,h in [(a,b,c) for a in range(M) for b in range(N) for c in range(H)]:
    if distance[h][j][i] == 999:
        if not array[h][j][i]:
            print(-1)
            break
    else:
        if distance[h][j][i] > rst:
            rst = distance[h][j][i]
else:
    print(rst)

