delta = [(1,0),(0,1),(-1,0),(0,-1)]
import copy

def pprint(table):
    for row in table:
        print(row)
    print()
    return


def solve(n,w,h,table):
    global rst
    
    def gravity(table):
        for i in range(H-1, 0, -1):
            for j in range(W):
                if table[i][j] == 0:
                    table[i][j], table[i-1][j] = table[i-1][j], table[i][j]
        return 

    def bomb(y,x,table):
        bombN = table[y][x]
        pprint(table)
        if bombN > 0:
            table[y][x] = 0
            for dlt in delta:
                cnt = 0
                while cnt < bombN:
                    ny , nx = y + dlt[0], x + dlt[1]
                    if 0 <= ny < H and 0 <= nx < W and table[ny][nx]:
                        bomb(ny,nx,table)
                    cnt += 1
        return 

    def findstart(table):
        starts = []
        for j in range(W):
            for i in range(H):
                if table[i][j]:
                    starts.append((i,j))
                    break 
        return starts
                
    def countblocks(table):
        cnt = 0
        for i in range(H):
            for j in range(W):
                if table[i][j]:
                    
                    cnt += 1    
        return cnt
    
    if n <= 0:
        if rst > countblocks(table):
            rst = countblocks(table)
            return
    else:
        starts = findstart(table)        
        if starts:
            for y,x in starts:
                workspace = copy.deepcopy(table)
                bomb(y,x,workspace)
                gravity(workspace)
                solve(n-1,w,h,workspace)
    return rst

T = int(input())
for test_case in range(1,T+1):
    N, W, H  = map(int, input().split())
    array = [list(map(int,input().split())) for _ in range(H)]
    rst = 100000
    print(solve(N,W,H,array))
        