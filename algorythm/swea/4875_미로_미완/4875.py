'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100
 
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
'''
def validway(y,x,table):
    global N
    if y > 0 and table[y-1][x] not in ['1','X']:
        return y - 1 , x, True
    elif x+1 < N and table[y][x+1] not in ['1','X']:
        return y , x + 1, True
    elif x > 0 and table[y][x-1] not in ['1','X']:
        return y, x - 1, True
    elif y+1 < N and table[y+1][x] not in ['1','X']:
        return y + 1 , x, True
    else:
        return y, x , False

def pr(table,cnt,y,x):
    print(cnt,y,x,stack)
    for idx in range(N):
        print(table[idx])
    print()
    return        

T = int(input())
for test_case in range(1,T+1):
        rst = 0
        N = int(input())
        table = [list(map(str,input())) for _ in range(N)]
        # print(table)        
        for i in range(N):    
            for j in range(N):
                if table[i][j] == '2':
                    y = i
                    x = j
        stack = [(y,x)]
        cnt = 0
        while True:
            cnt += 1
            
            if table[y][x] == '3':
                rst = 1
                break                
            table[y][x] = 'X'
            pr(table,cnt,y,x)
            y, x , valid = validway(y,x,table)
            stack.append((y,x))
            
            if valid is False: # noway    
                if stack:
                    y, x = stack.pop()
                else:
                    rst = 0
                    break
        print(f'#{test_case} {rst}')