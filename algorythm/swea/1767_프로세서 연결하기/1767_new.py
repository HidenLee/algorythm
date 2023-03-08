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


def func(remain,core_N,table):
    global min_lines
    global max_core_N
    if len(remain) + core_N <= max_core_N:
        return
    if remain:
        y, x = remain.pop()
    else:
        return
    workspace = copy.deepcopy(table)
    sides = []
    aimed_on = []
    sides.append([(y,j) for j in range(N) if j > x]) # 오른쪽
    sides.append([(y,j) for j in range(N) if j < x]) # 왼쪽
    sides.append([(i,x) for i in range(N) if i < y]) # 위쪽
    sides.append([(i,x) for i in range(N) if i > y]) # 아래쪽
    temp_line_n = N
    for side in sides:
        if not 1 in [workspace[i][j] for i,j in side] and temp_line_n > len(side):
            temp_line_n = len(side)
            aimed_on = side
    else:
        if aimed_on:
            for i,j in aimed_on:
                workspace[i][j] = 1
                func(remain,core_N+1,workspace)
            print(y,x,aimed_on)
            pprint(workspace)
        else: #aimed on이 비어있다는건 어느쪽으로도 손을 못 뻗는 코어라는 뜻
            return
    lines = sum(sum(workspace,[])) - M
    if max_core_N < core_N: # 코어 신기록~
            max_core_N = core_N # 신기록 갱신
            min_lines = lines # 줄수 판정
    elif max_core_N == core_N and min_lines > lines: # 코어가 같을때 줄이 더 짧은걸 선호
            min_lines = lines
            pprint(workspace)

    return min_lines

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
    corelist = []
    max_core_N = 0
    min_lines = 1e9
    for i in range(0,N):
        for j in range(0,N):
            if array[i][j]:
                if i in [0,N-1] or j in [0, N-1]:
                    max_core_N += 1
                else:
                    corelist.append((i,j))
    M = len(corelist)
    print(func(corelist,max_core_N,array))
