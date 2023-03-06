T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    array = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            # 십자
            target1 = [(y,x) for y in range(i-M+1,i+M) for x in range(j-M+1,j+M) if 0 <= y < N and 0 <= x < N and (y == i or x == j)]
            fly = sum([array[y][x] for y,x in target1])
            if ans < fly:
                ans = fly
            # 엑스
            target2 = [(y,x) for y in range(i-M+1,i+M) for x in range(j-M+1,j+M) if 0 <= y < N and 0 <= x < N and (y+x == i+j or y-x == i-j)]
            fly = sum([array[y][x] for y,x in target2])
            if ans < fly:
                ans = fly
    print(f'#{test_case} {ans}')
    
    
    
## 예훈s
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pari_max = 0
    d_p = ((0,-1),(0,1),(-1,0),(1,0)) # 좌우상하
    d_x = ((-1,-1),(-1,1),(1,-1),(1,1)) # 대각선
    for i in range(N):
        for j in range(N):
            p_hap = [arr[i][j]]
            x_hap = [arr[i][j]]
            for k in range(4): # 4방향 탐색
                for mul in range(1, M): # 한 방향에서 M까지 탐색
                    ni = i + mul * d_p[k][1]
                    nj = j + mul * d_p[k][0]
                    if 0 <= ni < N and 0 <= nj < N:
                        p_hap.append(arr[ni][nj])
                    nii = i + mul * d_x[k][1]
                    njj = j + mul * d_x[k][0]
                    if 0 <= nii < N and 0 <= njj < N:
                        x_hap.append(arr[nii][njj])
            if sum(p_hap) > pari_max:
                pari_max = sum(p_hap)
            elif sum(x_hap) > pari_max:
                pari_max = sum(x_hap)
 
    print(f'#{tc} {pari_max}')