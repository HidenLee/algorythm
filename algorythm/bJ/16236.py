from collections import deque
delta = [(-1,0),(0,-1),(0,1),(1,0)]
def expup():
    global level
    global exp
    exp += 1
    if exp == level:
        level +=1
        exp = 0
    return

def gototarget(y,x, depth):
    global ans
    global target
    global stack
    print(y,x,level)
    arr[y][x] = 0
    ans += depth
    expup()
    findfish(y,x)

def findfish(y,x):
    visited = [[False]*N for _ in range(N)]
    target = []
    q = deque([(y,x,1)])
    stack = [q]
    while stack:
        queue = stack.pop()
        while queue:
            oy, ox, depth = queue.popleft()
            for dlt in delta:
                ny, nx = oy + dlt[0], ox + dlt[1]
                if 0<= ny < N and 0 <= nx < N and not visited[ny][nx]: 
                    visited[ny][nx] = True
                    if arr[ny][nx] > level:
                        continue
                    if 0< arr[ny][nx] < level:
                        if not target or target[0][2] == depth:
                            target.append((ny,nx,depth))
                    queue.append((ny,nx,depth+1))
        if target:
            target.sort(key=lambda X : (-X[2],X[0],X[1]))
            gototarget(*target[0])
    return ans

N = int(input())
level = 2
exp = 0
ans = 0
arr = [[] for _ in range(N)]
for i in range(N):
    temp = list(map(int,input().split()))
    if 9 in temp:
        now = (i,temp.index(9))
        temp[now[1]] = 0
    arr[i] = temp
print(findfish(now[0],now[1]))