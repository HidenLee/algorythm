'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.


[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
import sys
sys.stdin = open('sample_input.txt','r')


def minmax(): #최소와 최대를 구해서 그 차를 반환
    N = int(input()) # N개의 수를 입력받을 예정
    numbers = list(map(int,input().split())) # 입력 받은 숫자들 리스트로 저장
    # return max(numbers) - min(numbers) 이러면 쉽겠지만..
    def my_max(list1): # 최대를 구하는 함수
        temp = 0
        for elm in list1: # 리스트의 각 요소가
            if temp < elm: # 기존 저장 값보다 크면
                temp = elm # 덮어쓰기
        return temp        


    def my_min(list1):
        temp = float('inf') # 'inf'는 매우 큰 수
        for elm in list1:
            if temp > elm: # 기존 저장 값보다 작으면
                temp = elm # 덮어쓰기
        return temp
    return my_max(numbers) - my_min(numbers) #최댓값에서 최솟값을 뺴면 절댓값 고려 필요 X



t= int(input()) # 테스트케이스 수
for test_case in range(t):
    print(f'#{test_case+1} {minmax()}') # 지정된 출력 예시에 맞춰 출력