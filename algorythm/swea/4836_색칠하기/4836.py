'''
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 
칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
주어진 정보에서 같은 색인 영역은 겹치지 않는다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
color = 1 (빨강), color = 2 (파랑)

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    colors = [[],[]]
    for color in range(N):
        xys = []
        r1, c1, r2 , c2 , coloridx = map(int,input().split())
        for rows in range(r2-r1+1):
            for cols in range(c2-c1+1):
                xys.append((r1+rows,c1+cols))
        colors[coloridx-1] += xys
    colors[0] = list(set(colors[0]))
    colors[1] = list(set(colors[1]))
    cnt = 0
    for dot in colors[1]:
        if dot in colors[0]:
            cnt += 1
    print(f'#{test_case} {cnt}')        
