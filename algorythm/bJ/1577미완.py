N, M = map(int, input().split())
cal = [[0 for _ in range(M)] for _ in range(N)]
trap = {}
for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    trap[a*M+b] = (c,d)
    trap[c*M+d] = (a,b)
for i in range(N):
    if i * M in trap and trap[i*M] == (i+1,0):
        break 
    cal[i][0] = 1
for i in range(M):
    if i in trap and trap[i] == (0,i+1):
        break
    cal[0][i] = 1

# from collections import deque
# delta = [(1,0),(0,1),(-1,0),(0,-1)]
# def bfs(node):
#     deq = deque([node])
#     while deq:
#         ox,oy = deq.popleft()
#         for dt in delta:
#             nx,ny = ox+dt[0], oy+dt[1]
#             if ox + oy * M in trap and trap[ox+oy*M] ==  (nx,ny):
#                 continue
                
#             if 0<= nx < M and 0<= ny < N:
#                 deq.append((nx,ny))
#                 cal[ny][nx] += 1

