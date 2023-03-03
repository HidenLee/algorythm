import sys
sys.stdin = open('algorythm\\swea\\5656_벽돌깨기\\input.txt','r')
sys.stdout = open('algorythm\\swea\\5656_벽돌깨기\\output.txt','w')


import copy

delta = [(1,0),(0,1),(-1,0),(0,-1)]

def pprint(table): # 디버깅을 위해 만든 array출력 함수
    for row in table:
        print(row)
    print()
    return


def solve(n,w,h,table): # rst (남은 블록 수) 반환
    global rst
    
    def gravity(table): # 아래부터 탐색, 0일때 위쪽에서 가장 가까운 값을 찾아와서 서로 교체
        for j in range(W):
            for i in range(H-1, 0, -1):
                if table[i][j] == 0:
                    for x in range(1,i+1):
                        if table[i-x][j]:
                            table[i][j], table[i-x][j] = table[i-x][j], table[i][j]
                            break
        return        

    def bomb(y,x,table): # 폭탄 펑펑 
        bombN = table[y][x]
        if bombN > 0:
            table[y][x] = 0
            for dlt in delta:
                cnt = 1
                ny, nx = y, x
                while cnt < bombN:
                    ny , nx = ny + dlt[0], nx + dlt[1]
                    cnt += 1
                    if 0 <= ny < H and 0 <= nx < W:
                        bomb(ny,nx,table)                    
        return 

    def findstart(table): # 폭탄은 항상 위에서 떨어지기때문에! 만약 반환되는 리스트가 비어있다면 어레이 전체가 비었다는 뜻
        starts = []
        for j in range(W):
            for i in range(H):
                if table[i][j]:
                    starts.append((i,j))
                    break 
        return starts
                
    def countblocks(table): # 값을 가진 블럭들의 수를 반환
        cnt = 0
        for i in range(H):
            for j in range(W):
                if table[i][j]:
                    cnt += 1    
        return cnt

    if n == N: # 구슬을 다 썼을때 rst 최신화
        if rst > countblocks(table):
            rst = countblocks(table)
            return
    else: # 일반적인 함수 동작
        starts = findstart(table)        
        if starts:
            for y,x in starts:
                workspace = copy.deepcopy(table)
                bomb(y,x,workspace)
                gravity(workspace)
                solve(n+1,w,h,workspace)
        else:
            rst = 0
    return rst

T = int(input())
for test_case in range(1,T+1):
    N, W, H  = map(int, input().split())
    array = [list(map(int,input().split())) for _ in range(H)]
    rst = float('inf')
    print(f'#{test_case} {solve(0,W,H,array)}')
        