'''
[입력]

총 10개의 테스트케이스가 주어진다.

각 테스트케이스의 첫 번째 줄에는 건물의 개수 N이 주어진다. (4 ≤ N ≤ 1000)

그 다음 줄에는 N개의 건물의 높이가 주어진다. (0 ≤ 각 건물의 높이 ≤ 255)

맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0이다. (예시에서 빨간색 땅 부분)
 
[출력]

#부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 조망권이 확보된 세대의 수를 출력한다.
'''
import sys
sys.stdin = open('input.txt','r')


def view(): # 조망권이 확보된 세대 수를 반환
    rownum = int(input()) # table에 받아올 줄 수
    table = list(map(int,input().split())) # 리스트의 형태로 입력값 저장

    goodlist = []
    
    for roop in range(2,rownum-2): # 각 줄에 대해
        # 지금 높이보다 크거나 높은 주변 두 칸의 빌딩을 묶은 리스트 
        # 주변 두 칸의 빌딩을 묶은 리스트
        smallist = table[roop-2:roop+3]
        if max(smallist) == table[roop]:
            smallist.sort() # 오름차순 정렬 (타겟 건물이 가장 큰값을 가지길 바래)
            temp = smallist[-1] - smallist[-2]
            if temp != 0: # 동점도 포함할까봐 조건 하나더 달아줌
                goodlist.append(temp)
    # print(goodlist)
    return sum(goodlist) # 그래서 총 몇 세대냐!!



t= 10 # 10개의 테스트케이스
for test_case in range(t):
    print(f'#{test_case+1} {view()}') # 지정된 출력 예시에 맞춰 출력