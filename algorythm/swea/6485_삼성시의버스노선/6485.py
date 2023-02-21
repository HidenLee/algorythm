'''
[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N ( 1 ≤ N ≤ 500 )이 주어진다.
다음 N개의 줄의 i번째 줄에는 두 정수 Ai, Bi ( 1 ≤ Ai ≤ Bi ≤ 5,000 )가 공백 하나로 구분되어 주어진다.
다음 줄에는 하나의 정수 P ( 1 ≤ P ≤ 500 )가 주어진다.
다음 P개의 줄의 j번째 줄에는 하나의 정수 Cj ( 1 ≤ Cj ≤ 5,000 ) 가 주어진다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 칸을 띄운 후,
한 줄에 P개의 정수를 공백 하나로 구분하여 출력한다.
j번째 정수는 Cj번 버스 정류장을 지나는 버스 노선의 개수여야 한다.
# '''

# import sys
# sys.stdin = open('s_input.txt','r')

T = int(input()) # 테스트케이스의 수
for test_case in range(T):
    N = int(input()) # 운영하는 버스의 수
    buslist = [(0,0)]*N #(출발지,도착지) - 튜플의 형태로 버스목록을 받기 위해 리스트 초기화
    for roop in range(N):
        buslist[roop] = tuple(map(int,input().split()))
    P = int(input()) # 버스 정류장의 수
    stoplist = [0]*P # 리스트의 형태로 정류소 목록을 받기 위해 초기화
    result = [0]*P # 결과를 출력할 리스트
    for roop in range(P):
        stoplist[roop] = int(input()) # 정류장의 번호를 입력받았을때
        count = 0
        for bus in buslist:
            if stoplist[roop] in range(bus[0],bus[1]+1): #그 번호가 특정 버스의 이동경로에 포함된다면
                count +=1 # 카운트롤 올리고
        result[roop] = count # 그 정류장을 위한 모든 버스의 탐색이 끝났을때 result 리스트에 카운트값 저장
    print(f'#{test_case+1}',end=' ') # 출력양식을 맞추기위해 포맷팅 활용
    print(*result,sep=' ')           # 리스트의 요소만 출력하기위해 asterlisk사용  
