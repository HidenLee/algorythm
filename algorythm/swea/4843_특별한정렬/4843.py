'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 
큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
10 1 9 2 8 3 7 4 6 5
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.
'''
def selectsmall(arr,n):
    for i in range(0,n):
        mindex = i
        for j in range(i+1,len(arr)):
            if arr[mindex] > arr[j]:
                mindex = j
        arr[i], arr[mindex] = arr[mindex], arr[i]
    return arr

def selectbig(arr,n):
    for i in range(0,n):
        maxdex = i
        for j in range(i+1,len(arr)):
            if arr[maxdex] < arr[j]:
                maxdex = j
        arr[i], arr[maxdex] = arr[maxdex], arr[i]
    return arr
    


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    list1 = list(map(int,input().split()))
    biglist = selectbig(list1[:],N)
    smalllist = selectsmall(list1[:],N)
    rst = []
    for roop in range(N):
        rst.append(biglist[roop])
        rst.append(smalllist[roop])
    rst = rst[:10]
    print('#', end='')
    print(test_case, end='')
    print(' ', end='')
    print(*rst)
    