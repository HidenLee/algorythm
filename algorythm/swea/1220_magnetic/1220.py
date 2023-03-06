'''
[입력]
테이블 위에 자성체들이 놓여 있다.
자성체들은 성질에 따라 색이 부여되는데, 푸른 자성체의 경우 N극에 이끌리는 성질을 가지고 있고, 
붉은 자성체의 경우 S극에 이끌리는 성질이 있다.
아래와 같은 테이블에서 일정 간격을 두고 강한 자기장을 걸었을 때, 
시간이 흐른 뒤에 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구하라.
아래는 자성체들이 놓여 있는 테이블을 위에서 바라본 모습이다.
자성체는 테이블 앞뒤 쪽에 있는 N극 또는 S극에만 반응하며 자성체끼리는 전혀 반응하지 않는다.
10개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 정사각형 테이블의 한 변의 길이가 주어진다. (이 값은 항상 100이다)
그 다음 줄부터 100 x 100크기의 테이블의 초기 모습이 주어진다. 1은 N극 성질을 가지는 자성체를 
2는 S극 성질을 가지는 자성체를 의미하며 테이블의 윗부분에 N극이 아래부분에 S극이 위치한다고 가정한다.
(N극 성질을 가지는 자성체는 S극에 이끌리는 성질이 있다.)

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 교착 상태의 개수를 출력한다.
'''
import sys
sys.stdin = open('C:\\Users\\SSAFY\\Desktop\\HDHD\\1학기\\algorythm\\algorythm\\swea\\1220_magnetic\\input.txt','r')

for test_case in range(1,11):
    N = int(input())
    array = [[] for _ in range(N)]
    for _ in range(N):
        temp = list(map(int,input().split()))
        for idx in range(len(temp)):
            if temp[idx] in [1,2]:
                array[idx].append(temp[idx])
    
    
    
    
    
    newray = []  
    
    for rows in array:
        lidx, ridx = 0, 1
        if rows[0] == 2:
            lidx = rows.index(1)
        if rows[-1] == 1:
            temp = list(reversed(rows))
            ridx = temp.index(2)
            newray.append(rows[lidx:-ridx])
        else:
            newray.append(rows[lidx:])    
    cnt = 0
    for rows in newray:    
        newnewray = [rows[0]]
        for idx in range(len(rows)):# 112 ->12
            if newnewray[-1] != rows[idx]:
                newnewray.append(rows[idx])
        cnt += int(len(newnewray)/2)        
        # print(rows,'\n',newnewray,cnt)        


        
        
          
    print(f'#{test_case} {cnt}')