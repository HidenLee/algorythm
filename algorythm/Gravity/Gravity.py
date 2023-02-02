import sys
sys.stdin = open('input.txt','r')

def gravity(): # 최대 낙차를 구하는 함수
    rownum = int(input()) # table에 받아올 줄 수
    table = list(map(int,input().split())) # 리스트의 형태로 입력값 저장

    #상자들은 모두 벽면에 붙여진 상태로 쌓여 벽에서 떨어져 쌓인 상자가 없다는 지문에서 착안,
    #특정 줄에서 가장 낙차가 큰 상자가 나온다면, 그 상자는 그 줄의 가장 꼭대기에 위치할 것이라고 전제

    temp = 0
    nakchalist = []
    
    for roop in range(rownum-1): # 각 줄에 대해
        
        # 지금 높이보다 크거나 높은 오른쪽 상자들을 묶은 리스트 
        smallist = list(x for x in table[roop+1:] if x>=table[roop]) 
        
        #낙차 = 내 위치(왼쪽부터 시작하기떄문에 루프의 역순)-스몰리스트의 크기(오른쪽에 나보다 높은 상자들의 수)
        nakchalist.append((rownum-1)-roop-len(smallist)) 
    
    return max(nakchalist) # 낙차들의 모임에서 가장 큰 값을 반환


t= int(input()) # 테스트케이스 수
for test_case in range(t):
    print(f'#{test_case+1} {gravity()}') # 지정된 출력 예시에 맞춰 출력