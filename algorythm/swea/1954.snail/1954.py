T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    nums = list(reversed(range(1,N**2+1)))
    array = [[0]*N for _ in range(N)]
    array[0][0] = nums.pop() 
    y, x = 0 , 0
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    direction = 0
    while nums != []:
        nexty , nextx = y+delta[direction][0], x+delta[direction][1]
        if 0<=nextx<N and 0<=nexty<N and array[nexty][nextx] == 0:
            y , x = nexty , nextx
            array[y][x] = nums.pop()
        else:
            direction += 1
            if direction >= 4:
                direction -= 4    
    
    print(f'#{test_case}')
    for rows in array:
        print(*rows)