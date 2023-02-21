''' 
(0,0) ~ (15,15) 256칸의 미로
시작점은 (1,1), 도착점은(13,13)로 고정
지역값 0은 길, 1은 벽, 2는 시작점, 3은 도착점
해결 가능한 미로라면 1을 반환, 불가능하면 0을 반환
'''
# 미로의 성공여부를 판단하는 함수, 미로는 2-D array로 인풋예정
# 10개의 테스트케이스/// 각 테스트케이스의 넘버\n미로가 인풋

def maze1(target):
    size = len(target)
    for col in range(size):
        for row in range(size):
            if target[row][col] == 2:
                x = col
                y = row
    #calibrating
    nodelist = []
    visitlist = []
    for roop in range(size):
        visitlist.append([])
    for roop in range(size):
        for num in target[roop]:
            if num == 1:
                visitlist[roop].append(True)
            else:
                visitlist[roop].append(False)       
    ismaze = 1
 
    #탐색, y,x를 반환
    def check(y,x):
        nonlocal ismaze 
        #갈림길인지 판단하는 함수(반환값 1:일방길 0:막힌길, 2~:갈림길)
        def roadshape(y,x):
            temp = 0
            if target[y][x+1] != 1 and visitlist[y][x+1]==False:
                temp += 1
            if target[y+1][x] != 1 and visitlist[y+1][x]==False:
                temp += 1
            if target[y][x-1] != 1 and visitlist[y][x-1]==False:
                temp += 1
            if target[y-1][x] != 1 and visitlist[y-1][x]==False:
                temp += 1 
            return temp

        if roadshape(y,x) == 0:    
            if nodelist == []: 
                # 노드리스트 비었으면 미로를찢어
                ismaze = 0
                return y,x
            # 마지막 노드로 돌아가기
            else:
                y,x = nodelist.pop()
                return y,x
        elif roadshape(y,x) > 1:
            #갈림길이면 노드 저장
            nodelist.append((y,x))
            return y,x  
        else: # 일방길
            return y,x 

    def goaheadwhile():
        count = 0
        nonlocal x
        nonlocal y
        nonlocal ismaze
        while ismaze != 0:
            if count > 3000:
                break
            # print(x,y,count)
            if target[y][x] == 3:
                ismaze = 1
                break
            count += 1
            visitlist[y][x] = True
            y,x = check(y,x)

            if target[y][x+1] != 1 and visitlist[y][x+1]==False:
                x = x+1
            elif target[y-1][x] != 1 and visitlist[y-1][x]==False:
                y = y-1
            elif target[y][x-1] != 1 and visitlist[y][x-1]==False:
                x = x-1
            elif target[y+1][x] != 1 and visitlist[y+1][x]==False:
                y = y+1
            else:    
                ismaze = 0
                return          

    while ismaze == 1:
        goaheadwhile()
        if target[y][x] == 3:
            break
    return ismaze    

# 테스트케이스를 입력~ 함수돌리고 각각 출력~
import sys
sys.stdin = open("1학기\\algorythm\\algorythm\\swea\\1226_미로1\\input.txt", "r")
N = 16
for testcase in range (10):
    t = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    print(f'#{t} {maze1(maze)}')



