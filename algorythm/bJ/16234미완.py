#https://www.acmicpc.net/problem/16234
N, L, R = map(int,input().split())
world = [ list(map(int,input().split())) for _ in range(N)]
delta = [(1,0),(0,1),(-1,0),(0,-1)]
day = 0

def pprint(arr):
    print("pprint")
    for _ in range(len(arr)):
        print(arr[_])

        
while day <= 2000:
    flag = True
    # visit = [ [False] * N for _ in range(N) ]
    newworld = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if newworld[i][j]:
                continue
            stack = [(i,j)]
            union = set([(i,j)])
            while stack:
                ox, oy = stack.pop()
                # visit[ox][oy] = True
                for dx, dy in delta:
                    nx, ny = ox + dx, oy + dy
                    if 0 <= nx < N and 0 <= ny < N and L <= abs(world[ox][oy]-world[nx][ny]) <= R :
                        if not (nx,ny) in union:
                        # print(ox,oy,nx,ny)
                            stack.append((nx,ny))
                        union.add((nx,ny))
            # print(union)
            if len(union) >= 2:
                flag = False
            avr = sum([world[x][y] for x,y in union]) // len(union)
            for tx,ty in union:
                newworld[tx][ty] = avr
    pprint(newworld)
    world = newworld
    if flag:
        print(day)
        break
    day += 1
