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
    #calibrating
    nodelist = []
    visitlist = [[False]*size for _ in range(size)]
    
    for row in range(size):
            if 2 in target[row]:
                y = row
                x = target[row].index(2)
                target[y][x] = 1
    
    delta = [(1,0),(0,-1),(-1,0),(0,1)]
    ismaze = True
    while ismaze:
        if target[y][x] == 3:
            break      
        else:
            visitlist[y][x] = True
        for dlt in delta:
            if 0 <= y + dlt[0] < size and 0 <= x + dlt[1] < size and visitlist[y+dlt[0]][x+dlt[1]] == False and target[y+dlt[0]][x+dlt[1]] != 1:
                nodelist.append((y,x))
                y = y + dlt[0]
                x = x + dlt[1]
                break
        else:
            if nodelist:
                y , x = nodelist.pop()
            else:
                ismaze = False
                break
    return ismaze        
# 테스트케이스를 입력~ 함수돌리고 각각 출력~
import sys
sys.stdin = open("1학기\\algorythm\\algorythm\\swea\\1226_미로1\\input.txt", "r")
N = 16
for testcase in range (10):
    t = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    print(f'#{t} {int(maze1(maze))}')



