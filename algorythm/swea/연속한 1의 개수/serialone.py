'''
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.

입력
첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N, 다음 줄에 N개의 0과1로 구성된 수열이 공백없이 제공된다.
1<=T<=10, 10<=N<=1000

출력
#과 테스트케이스 번호, 빈칸에 이어 답을 출력한다.
'''
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    nums = int(input())
    temp = 0
    cnt = 0
    while N >= 0:
        if nums % 10:
            cnt += 1
        else:
            if cnt > temp:
                temp = cnt
            cnt = 0
        nums = nums // 10
        N -= 1
    print(f'#{test_case} {temp}')