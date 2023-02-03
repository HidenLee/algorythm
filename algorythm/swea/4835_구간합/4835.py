'''
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
import sys
sys.stdin = open('sample_input.txt','r')


def guganhap(): #최소와 최대를 구해서 그 차를 반환
    N, M = map(int,input().split()) # N과 M을 입력
    numbers = list(map(int,input().split())) # 입력 받은 숫자들 리스트로 저장
   
    sumlist = [] 
    for broop in range(N-M+1): # 반복문으로 원하는 합계들의 리스트를 생성
        sumn = 0
        for sroop in range(M):
           sumn += numbers[broop+sroop]  
        sumlist.append(sumn)


    return max(sumlist) - min(sumlist) #최댓값에서 최솟값을 뺴면 절댓값 고려 필요 X



t= int(input()) # 테스트케이스 수
for test_case in range(t):
    print(f'#{test_case+1} {guganhap()}') # 지정된 출력 예시에 맞춰 출력