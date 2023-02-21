'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
def comb(iterable,N): # 부분집합의 모음 리스트를 반환하는 함수
    n = len(iterable)
    temp = []
    rst = []
    for i in range(1<<n): # 1<<n == 2**n # 공집합을 포함해서 2^n개의 모든 부분집합을 표현가능
        for j in range(n): # 각 원소를 순회하며
            if i & (1<<j): # 각 원소가 타겟 부분집합의 원소라면
                temp.append(iterable[j]) # 임시 리스트에 저장
        if len(temp) == N: # 우리가 원하는 크기의 부분집합만
            rst.append(temp) #결과 리스트에 저장
        temp=[]   # 반복 돌때마다 임시리스트 초기화
    return rst # 결과 리스트 반환


A = list(range(1,13))
T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    comblist = comb(A,N)
    cnt = 0
    for com in comblist:
        if sum(com) == K:
            cnt += 1
    print(f'#{test_case} {cnt}')





       

