# https://www.acmicpc.net/problem/13565

N, M = map(int,input().split())
table = [str(input()) for _ in range(N)]
delta = [(1,0),(0,-1),(-1,0),(0,1)]
ans = False
for idx, start in enumerate(table[0]):
    if int(start) or ans:
        continue
    stack = [(0,idx)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    while stack:
        y, x = stack.pop()
        if y == N-1 :
            ans = True
            break

        visited[y][x] = True
        for dy, dx in delta:
            ny, nx = y + dy, x+ dx
            if 0<= ny and ny < N and 0<= nx and nx < M  and not int(table[ny][nx]) and not visited[ny][nx]:
                stack.append((ny,nx))
if ans:
    print("YES")
else:
    print("NO")