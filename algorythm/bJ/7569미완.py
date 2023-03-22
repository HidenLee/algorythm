from collections import deque
delta = [(0,0,1),(0,0,-1),(0,-1,0),(0,1,0),(1,0,0),(-1,0,0)]
import sys
sys.stdin = open('algorythm\\bJ\\input.txt','r')



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
        visited = set()
        nxts = deque([(i,j,h)])
        while nxts:
            (i,j,h) = nxts.popleft()
            neighbor = [(i+dlt[0],j+dlt[1],h+dlt[2]) for dlt in delta if 0<=i+dlt[0]<M and 0<=j+dlt[1]<N and 0<=h+dlt[2]<H and not array[h+dlt[2]][j+dlt[1]][i+dlt[0]]]
            for ni,nj,nh in neighbor:
                if distance[nh][nj][ni] > distance[h][j][i]:
                    distance[nh][nj][ni] = distance[h][j][i] + 1
                    if not (ni,nj,nh) in visited:
                        nxts.append((ni,nj,nh))
                        visited.add((i,j,h))
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


