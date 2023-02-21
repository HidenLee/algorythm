'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. 
NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
 
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

def check(list1): # arg로 받은 리스트의 요소가 회문인지 판단하는 함수 / 반환값 = True or False
    n = len(list1) # 리스트의 길이가 짝수일때와 홀수일때로 구분
    if n % 2 == 0 : 
        for roop in range(int(n/2)): 
            if list1[roop] != list1[-roop-1]:
                return False  
    else:
        for roop in range(int((n-1)/2)):       
            if list1[roop] != list1[-roop-1]:
                return False
    return True


T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split()) # 해당 케이스에서 판단하고싶은 회문의 길이
    # rst = [] # 원하는 결과 값의 횟수를 세기 위한 변수
    array = [] # nbyn 어레이가 들어갈 빈 리스트
    for _ in range(N):
        array.append(input())
        for idx in range(N-M+1): # 가로로 받으면서 바로 확인
            if check(array[-1][idx:idx+M]): # 회문이라면!
                rst = array[-1][idx:idx+M]
                # print('가로',array[-1][idx:idx+N])           
    for cols in range(N): # 이번엔 세로로 세야하는데 
        for idx in range(N-M+1):
            newray = []
            for roop in range(M):
                newray.append(array[idx+roop][cols])
            if check(newray):
                rst = ''.join(newray)
                # print('세로',cols,newray)    

    print(f'#{test_case} {rst}')