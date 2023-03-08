import copy

import sys
sys.stdin = open('algorythm\\algorythm\\swea\\1767_프로세서 연결하기\\input.txt','r', encoding="utf8")
sys.stdout = open('algorythm\\algorythm\\swea\\1767_프로세서 연결하기\\output.txt','w', encoding="utf8")


delta = [(1,0),(0,1),(-1,0),(0,-1)]


def pprint(table):
    '''
    디버깅을 위해 만든 array출력 함수
    '''
    for row in table:
        print(row)
    print()



def drawline(lst,core,lines,table):
    global minline
    global maxcore
    if len(lst) + core <= maxcore: # 가망없는 경우의수
        return
    if maxcore < core: # 코어 신기록~
        maxcore = core # 신기록 갱신
        minline = lines # 줄수 판정

    elif maxcore == core and minline > lines: # 코어가 같을때 줄이 더 짧은걸 선호
        minline = lines
    workspace = copy.deepcopy(table)
    y, x = lst.pop()
    stack = [[] for _ in range(4)]
    temp = 1e9
    for idx in range(4):
        ny, nx = y, x
        while True:
            ny, nx = ny + delta[idx][0], nx + delta[idx][1]
            if 0 <= ny < N and 0 <= nx < N:
                if workspace[ny][nx] == 1: # 이 방향은 안돼
                    stack[idx] = []
                    break
                else:
                    stack[idx].append((ny,nx))
            else: # out of range, 전원 연결 성공
                if temp >= len(stack[idx]): # 이 방향이 최선이야!
                    temp = len(stack[idx])
                    for jdx in range(4): # 다른 방향으로 그린 전선 제거
                        for i,j in stack[jdx]:
                            workspace[i][j] = 0

                    for i,j in stack[idx]: # 이 방향에서 선 긋기
                        workspace[i][j] = 1
                    if corelist: # 아직 설치할 코어가 남았면
                        print(test_case,corelist,minline)
                        pprint(table)
                        drawline(corelist,core+1,lines+temp,workspace)
                break
    return minline


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
    # visited = [[False]*N for _ in range(N)]
    corelist = []
    maxcore = 0
    minline = 1e9
    for i in range(1,N-1):
        for j in range(1,N-1):
            if array[i][j]:
                corelist.append((i,j))
    print(drawline(corelist,0,0,array))






'''
#sw아카데미 1767 프로세서 연결하기

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(depth,cnt,connect):
    global answer
    global max_connect
    if depth==l_c:
        if connect>max_connect:
            max_connect=connect
            answer=cnt
        elif connect==max_connect and answer>cnt:
            answer=cnt
        return
    #이렇게 반복문 형태로 돌려주면서 시간초과 줄여줬습니다.
    for k in range(depth,l_c):
        cx,cy=core[k]
        for d in range(4):
            nx=cx
            ny=cy
            flag=False
            tmp=set()
            leng=0
            #상하좌우 살피면서 연결여부를 판단
            while True:
                nx+=dx[d]
                ny+=dy[d]
                #범위벗어난다->연결이 되면 가능하다 표시하고 나가기
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    flag=True
                    break
                #코어를 만나면 못함
                if room[nx][ny]==1:
                    break
                #다른 전선을 만나면 못함
                tmp.add((nx,ny))
                leng+=1
            #가능하다면 전선을 연결
            if flag:
                for px,py in tmp:
                    room[px][py]=1
                #현재 연결한 코어 다음 코어로 넘어간다.
                dfs(k+1,cnt+leng,connect+1)

                for px,py in tmp:
                    room[px][py]=0


T=int(input())

for t in range(T):
    answer=1e9
    max_connect=0
    N=int(input())
    room=[]
    core=[]
    for i in range(N):
        tmp=list(map(int,input().split()))
        for j in range(1,N-1):
            if i==0 or i==N-1:
                break
            if tmp[j]==1:
                core.append([i,j])
        room.append(tmp)
    l_c=len(core)
    visited=[[False]*N for _ in range(N)]

    dfs(0,0,0)

    print("#%d %d"%(t+1,answer))
'''