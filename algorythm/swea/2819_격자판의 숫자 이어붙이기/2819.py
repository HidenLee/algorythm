delta = [(1,0),(0,1),(-1,0),(0,-1)]

def func1(y,x,depth,code):
    if depth == 7:
        pattern.add(code)
    else:
        for dlt in delta:
            ny, nx = y+dlt[0], x+dlt[1]
            if 0<=ny<4 and 0<=nx<4:
                func1(ny,nx,depth+1,code+arr[ny][nx])




for test_case in range(1, int(input())+1):
    arr = [list(map(str,input().split())) for _ in range(4)]
    pattern = set()
    for i in range(4):
        for j in range(4):
            func1(i,j,0,'')
    print(f'#{test_case} {len(pattern)}')
