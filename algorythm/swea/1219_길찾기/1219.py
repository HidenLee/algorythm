'''
도식화한 지도에서 A도시에서 출발하여 B도시로 가는 길이 존재하는지 조사하려고 한다.
길 중간 중간에는 최대 2개의 갈림길이 존재하고, 모든 길은 일방 통행으로 되돌아오는 것이 불가능하다.
다음과 같이 길이 주어질 때, A도시에서 B도시로 가는 길이 존재하는지 알아내는 프로그램을 작성하여라.
 - A와 B는 숫자 0과 99으로 고정된다.
 - 모든 길은 순서쌍으로 나타내어진다. 위 예시에서 2번에서 출발 할 수 있는 길의 표현은 (2, 5), (2, 9)로 나타낼 수 있다.
 - 가는 길의 개수와 상관없이 한가지 길이라도 존재한다면 길이 존재하는 것이다.
 - 단 화살표 방향을 거슬러 돌아갈 수는 없다.

[제약 사항]
출발점은 0, 도착점은 99으로 표현된다.
정점(분기점)의 개수는 98개(출발점과 도착점 제외)를 넘어가지 않으며, 한 개의 정점에서 선택할 수 있는 길의 개수도 2개를 넘어가지 않는다.

[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호와 길의 총 개수가 주어지고 그 다음 줄에는 순서쌍이 주어진다.
순서쌍의 경우, 별도로 나누어 표현되는 것이 아니라 숫자의 나열이며, 나열된 순서대로 순서쌍을 이룬다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.
'''
for test_case in range(10):
    T, N = map(int,input().split())
    temp = list(map(int,input().split()))
    newlist = [(lambda idx : (temp[idx],temp[idx+1]))(idx) for idx in range(2*N) if idx%2 ==0]
    stack = [0]
    visitted = [] 
    while stack:
        for tups in newlist:
            if tups[0] == stack[-1] and not tups[1] in visitted:
                stack.append(tups[1])
                break
        else: # 막다른길
            if stack != []:
                visitted.append(stack.pop())    
            else:
                break
    if 99 in visitted:
        ans = 1
    else:
        ans = 0
    print(f'#{T} {ans}')