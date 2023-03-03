delta = [(1,0),(0,1),(-1,0),(0,-1)]

def pprint(table):
    for row in table:
        print(row)
    print()
    return




    
def gravity(table):
    for j in range(W):
        for i in range(H-1, 0, -1):
            if table[i][j] == 0:
                for x in range(1,i+1):
                    if table[i-x][j]:
                        table[i][j], table[i-x][j] = table[i-x][j], table[i][j]
                        break
    return      

def bomb(y,x,table):
    bombN = table[y][x]
    # pprint(table)
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
                    # table[ny][nx] = 0                    
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


T = int(input())
for test_case in range(1,T+1):
    N, W, H  = map(int, input().split())
    array = [list(map(int,input().split())) for _ in range(H)]
    rst = 100000
    # print(test_case,solve(1,W,H,array))
    print(test_case)
    pprint(array)
    bomb(1,2,array)
    gravity(array)
    pprint(array)
    bomb(2,2,array)
    gravity(array)
    pprint(array)
    
        