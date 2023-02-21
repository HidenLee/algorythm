'''
주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.
[입력]
각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
총 10개의 테스트케이스가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.
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


T = 10
for test_case in range(1,T+1):
    t = int(input())
    temp = 0
    array = [] # 100by100 어레이가 들어갈 빈 리스트
    for _ in range(100):
        array.append(input())
        for N in range(2,101):
            for idx in range(100-N+1): # 가로로 받으면서 바로 확인
                if check(array[-1][idx:idx+N]): # 회문이라면!
                    if temp < N:
                        temp = N
                    # print('가로',array[-1][idx:idx+N])           
    
    for N in range(temp,101):
        for cols in range(100): # 이번엔 세로로 세야하는데 
            for idx in range(100-N+1):
                newray = []
                for roop in range(N):
                    newray.append(array[idx+roop][cols])
                if check(newray):
                    if temp < N:
                        temp = N
                    # print('세로',cols,newray)    

    print(f'#{test_case} {temp}')