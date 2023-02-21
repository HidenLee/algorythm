'''
8x8 평면 글자판에서 제시된 길이를 가진 회문의 개수를 구하라.

[입력]
총 10개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가 주어지며, 다음 줄에 8x8 크기의 글자판이 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 개수를 출력한다.
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


T = 1
for test_case in range(1,T+1):
    N = int(input()) # 해당 케이스에서 판단하고싶은 회문의 길이
    cnt = 0 # 원하는 결과 값의 횟수를 세기 위한 변수
    array = [] # 8by8 어레이가 들어갈 빈 리스트
    for _ in range(8):
        array.append(input())
        for idx in range(8-N+1): # 가로로 받으면서 바로 확인
            if check(array[-1][idx:idx+N]): # 회문이라면!
                cnt += 1
                # print('가로',array[-1][idx:idx+N])           
    for cols in range(8): # 이번엔 세로로 세야하는데 
        for idx in range(8-N+1):
            newray = []
            for roop in range(N):
                newray.append(array[idx+roop][cols])
            if check(newray):
                cnt += 1
                # print('세로',cols,newray)    

    print(f'#{test_case} {cnt}')