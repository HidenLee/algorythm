import sys
sys.stdin = open("input.txt", "r")

def palindrome(list_p): #list를 넣으면 이게 회문인지 아닌지 알려주는 함수
    for i in range(int(len(list_p)/2)):
        if list_p[i] == list_p[- i - 1]:
            pass
        else :
            return 0 #한번이라도 앞뒤가 다르다면 false
    return 1 # 끝까지 돌렸는데도 False 안나오면 list를 반환함

T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    total_list = []
    for i in range(N): #total list에 n*n 배열 만들어줌
        total_list.append(input().split())

        for j in range(N-M+1):
            if palindrome(total_list[-1][j:j+M]) == 1:
                print(f'#{t} {total_list[-1][j:j+M]}')
            else :
                pass
