#https://www.acmicpc.net/problem/1189

delta = [(0,-1),(1,0),(0,1),(-1,0)]

R, C, K = map(int, input().split())
table = [list(input()) for _ in range(R)]
def backtracking(x,y,depth,cnt):
    table[y][x] = depth
    if depth == K :
        if y == 0 and x == C - 1:
            return cnt + 1
        return cnt
    for dt in delta:
        nx = x + dt[0]
        ny = y + dt[1]
        if 0<= nx < C and 0 <= ny < R and table[ny][nx] == ".":
            cnt = backtracking(nx,ny,depth+1,cnt)
            table[ny][nx] = "."
    return cnt

print(backtracking(0,R-1,1,0))