# T = int(input())
# for test_case in range(1,T+1):
#     N = int(input())
#     array = [list(map(int,input().split())) for _ in range(N)]
#     maxroom = 0
#     delta = [(1,0),(0,1),(-1,0),(0,-1)]
#     searchlist = [divmod(sum(array,[]).index(X), N) for X in range(N**2,0,-1)]
#     for i , j in searchlist: 
#         if array[i][j] + maxroom <= N**2:


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
    maxroom = 0
    delta = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(N):
        for j in range(N):
            if array[i][j] + maxroom <= N**2:
                cnt = 1
                stack = [(i,j)]
                while stack:
                    y, x = stack.pop()
                    for dlt in delta:
                        if 0 <= y+dlt[0] < N and 0<= x+dlt[1] < N and array[y+dlt[0]][x+dlt[1]] == array[y][x] + 1:
                            stack.append((y+dlt[0],x+dlt[1]))
                            cnt += 1
                if maxroom < cnt:
                    maxroom = cnt
                    maxroomnum = array[i][j]
                elif maxroom == cnt and maxroomnum > array[i][j]:
                    maxroomnum = array[i][j]
    print(f'#{test_case} {maxroomnum} {maxroom}')