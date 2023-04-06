import sys
sys.stdin = open("algorythm\\swea\\1767_프로세서 연결하기\\in.txt",'r')

delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def route(y,x,d):
    r = [(y+d[0]*i,x+d[1]*i) for i in range(1,N) if 0<= y+d[0]*i < N and 0 <= x+d[1]*i < N]
    return r, not any([array[ny][nx] for ny,nx in r])


def func1(remaincore, nowcore, nowline, depth):
    global maxcore
    global minline
    
    if depth == M:  
        if  maxcore < nowcore or (nowcore == maxcore and minline > nowline):
            maxcore = nowcore
            minline = nowline
        return
        
    if M - sum(visited) + nowcore < maxcore:
        return
            
    for idx, target in enumerate(remaincore):
        targety, targetx = target
        if visited[idx]:
            continue
        for dlt in delta:
            r, route_valid = route(targety, targetx, dlt)
            if route_valid:
                visited[idx] = True
                for i,j in r: 
                    array[i][j] = 1                    
                func1(remaincore, nowcore+1, nowline+len(r),depth+1)
                for i,j in r: 
                    array[i][j] = 0
                visited[idx] = False
            else:
                visited[idx] = True
    print(depth)
    # for idx, target in enumerate(remaincore):
    #     if not visited[idx]:
    #         targety, targetx = target
    #         for dlt in delta:
    #             r, route_valid = route(targety, targetx, dlt)
    #             if route_valid:
    #                 visited[idx] = True
    #                 for i,j in r: 
    #                     array[i][j] = 1                    
    #                 func1(remaincore, nowcore+1, nowline+len(r))
    #                 for i,j in r: 
    #                     array[i][j] = 0
    #                 visited[idx] = False
            


for test_case in range(1,int(input())+1):
    N = int(input())
    remaincore = []
    array = []
    maxcore = 0
    minline = 9999
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(1,N-1):
            if row[j]:
                remaincore.append((i,j))
        array.append(row)
    M = len(remaincore)
    visited = [False]*M
    func1(remaincore, 0, 0, 0)
    print(f'#{test_case} {minline}')
