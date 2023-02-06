'''
[제약 사항]
1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.

[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

def lookup(array,y,x,k):
    rst = 0
    newx , newy = x , y
    if (0 <= y-1 and array[y-1][x] == 0) or y == 0: # 또 하나의 탐색조건, 세로는 위쪽에 앵커있는지 확인 
        cnt = 0
        while newy < len(array) and array[newy][x] != 0: # 끝까지 내려가거나 벽을 발견하면 스탑
            newy = newy + 1
            cnt += 1
        if cnt == k:
            # print(y,x,'세로')
            rst += 1
    newx, newy = x, y                 
    if (0 <= x-1 and array[y][x-1] == 0) or x == 0: # 가로는 왼쪽에 앵커있는지 확인 
        cnt = 0
        while newx < len(array) and array[y][newx] != 0: # 끝까지 옆으로 탐색하거나 벽을 발견하면 스탑
            newx = newx + 1
            cnt += 1
        if cnt == k:
            # print(y,x,'가로')
            rst += 1  
    return rst # 가로세로 둘다 충족하면 2반환, 하나만 충족하면 1반환, 충족하지않으면 0 반환

T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    array = []
    for _ in range(N):
        array.append(list(map(int,input().split())))
    result = 0
    for i in range(N):
        for j in range(N):
            if array[i][j] == 1: # 1의값을 가진 위치에서만 탐색시작
                result += lookup(array,i,j,K)
    print(f'#{test_case} {result}')                



