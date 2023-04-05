tunneldict = {0:[],1:[(0,1),(1,0),(0,-1),(-1,0)], 2:[(1,0),(-1,0)],3:[(0,1),(0,-1)],4:[(-1,0),(0,1)],5:[(1,0),(0,1)],6:[(0,-1),(1,0)],7:[(-1,0),(0,-1)]} 
# 각 터널 번호에 맞는 다음에 이어질수있는 방향을 딕셔너리 형태로 지정해뒀다.

def side(y,x,table): #리스트 컴프리헨션과 앞서 작성한 딕셔너리를 활용, 특정 칸에서 이어진 다음 칸을 리스트로 반환 (무방향 그래프 자료구조에서 이어지는 다른 노드를 탐색하는것과 같다.) 
    lst = [(y+dlt[0],x+dlt[1]) for dlt in tunneldict[table[y][x]] if 0 <= y+dlt[0] < N and 0 <= x+dlt[1] < M] 
    return lst


T = int(input())
for test_case in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(N)]
    queue= [(R,C,1)]
    visited = [[0]*M for _ in range(N)]
    while queue: # POP(0)와 append를 통해 bfs탐색, collections의 deque 구조를 활용했다면 더 효율적이였을 것이다.
        y, x, dist = queue.pop(0) # dist는 원점에서 부터의 거리를 의미한다, 탐색이 깊어질수록 1씩 증가한다.
        if dist <= L:
            visited[y][x] = 1    
            for nxty, nxtx in side(y,x,array):
                if not visited[nxty][nxtx] and (y,x) in side(nxty,nxtx,array):
                    queue.append((nxty,nxtx,dist+1))
    rst = sum(sum(visited,[])) # sum[1,2,3] == 1+2+3, sum[[1],[2]]=> error, sum[[1],[2],[]] ==[1]+[2]+[] == [1,2]
    print(f'#{test_case} {rst}')