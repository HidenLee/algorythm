def pprint(arr):
    for _ in range(len(arr)):
        print(arr[_])


#8방향 검사를 위한 델타 정의
delta = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)] 

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split()) 
    
    #처음 게임판의 구성
    table = [[0]*N for _ in range(N)]
    table[N//2-1][N//2-1] = 2
    table[N//2][N//2] = 2
    table[N//2][N//2-1] = 1
    table[N//2-1][N//2] = 1 
    
    #M번의 횟수동안 돌을 놓는다. 단순 반복을 위한 For 구문 활용
    for _ in range(M):
        y, x, c = map(int, input().split())
        # 게임판은 1,1이 시작이기때문에 인덱스를 맞춰준다.
        y = y - 1
        x = x - 1
        table[y][x] = c # c는 color을 의미, 돌을 놓았으니 게임판에 표기해준다.
        
        # 돌을 놓을때마다 델타 탐색을 통해 뒤집을 돌 판정,
        # 한개의 델타 방향에서 방금 놓은돌과 연속적으로 이어진 다른 색의 돌들의 좌표를 스택에 넣어둔다.
        # 방금 놓은 돌의 색이 다시 나타난다면 WBBBW이런꼴의 형태이기 때문에 가운데 갇혀있는 돌들(stack에 들어있는 좌표들)의 색을 바꿔준다.
        # 3-1 = 2, 3-2 = 1 => 다른 색깔을 표기할수있다. 
        for dlt in delta:
            stack = []
            ny, nx = y+dlt[0], x+dlt[1]
            while 0 <= ny < N and 0 <= nx < N: 
                if table[ny][nx] == 3-c:
                    stack.append((ny,nx))
                    ny += dlt[0]
                    nx += dlt[1]
                elif table[ny][nx] == c:
                    while stack:
                        ny,nx = stack.pop()
                        table[ny][nx] = c
                    break
                else:
                    break
        pprint(table)
                    
    #결과값 출력을 위한 카운트 변수 black, white
    black = white = 0            
    for elm in sum(table,[]):
        if elm == 1:
            black += 1
        if elm == 2:
            white += 1
    print(f'#{test_case} {black} {white}')