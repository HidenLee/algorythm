delta = delta = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    stones = []
    keepgoing = True
    for y in range(N):
        lst = list(input())
        for x in range(N):
            if lst[x] == 'o':
                stones.append((y,x))
    for y, x in stones:
        if keepgoing == False:
            break
        
        for dlt in delta:
            ny, nx = y , x
            cnt = 1
            while cnt < 5:
                ny, nx = ny + dlt[0], nx + dlt[1]
                if (ny, nx) in stones:
                    cnt += 1
                else:
                    break
            if cnt >= 5:
                print(f'#{test_case} YES')
                keepgoing = False
                break
    else:
        print(f'#{test_case} NO')
        