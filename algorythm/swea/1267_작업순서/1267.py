'''
해야 할 V개의 작업이 있다. 이들 중에 어떤 작업은 특정 작업이 끝나야 시작할 수 있으며, 이를 선행 관계라 하자.
이런 작업의 선행 관계를 나타낸 그래프가 주어진다.
이 그래프에서 각 작업은 하나씩의 정점으로 표시되고 선행 관계는 방향성을 가진 간선으로 표현된다.
단, 이 그래프에서 사이클은 존재하지 않는다 (사이클은 한 정점에서 시작해서 같은 정점으로 돌아오는 경로를 말한다).

이 그래프에서 작업 1은 작업 4가 끝나야 시작할 수 있다.
작업 6은 작업 5와 작업 7이 끝나야 할 수 있다.
김과장은 선행 관계가 주어진 작업군을 한 번에 하나의 작업씩 처리해서 다 끝내려 한다.
위에서 예를 든 작업군에 대해서 이런 일을 한다면 아래의 순서로 처리할 수 있다.
8, 9, 4, 1, 5, 2, 3, 7, 6
또한 아래의 순서도 가능하다.
4, 1, 2, 3, 8, 5, 7, 6, 9
아래의 순서는 가능하지 않다.
4, 1, 5, 2, 3, 7, 6, 8, 9
이 순서에서는 작업 5가 작업 8보다 먼저 처리되는데, 위 그래프에서 주어진 선행 관계에서는 작업 5는 작업 8이 끝나야 시작할 수 있어 이 순서로 끝내는 것은 가능하지 않다.
V개의 작업과 이들 간의 선행 관계가 주어질 때, 일을 끝낼 수 있는 작업 순서를 찾는 프로그램을 작성하라.
가능한 작업 순서가 여러 가지일 경우, 여러분은 이들 중 하나만 제시하면 된다.

[입력]
10개의 테스트케이스가 주어진다.
각 케이스의 첫번째 줄에는 그래프의 정점의 개수 V(3 ≤ V ≤ 1000)와 간선의 개수 E(2 ≤ E ≤ 3000)가 주어지고, 그 다음 줄에는 E개의 간선이 나열된다.
간선은 간선을 이루는 두 정점으로 표기된다.
예를 들어, 정점 5에서 28로 연결되는 간선은 “5 28”로 표기된다.
정점의 번호는 1부터 V까지의 정수값을 가지며, 입력에서 이웃한 수는 모두 공백으로 구분된다.

[출력]
각 케이스마다 ‘#x’(x는 테스트케이스의 번호이며 1부터 시작한다)를 출력하고 올바른 작업 순서를 공백으로 구분하여 출력한다.
'''
import sys
sys.stdin = open('algorythm\\algorythm\\swea\\1267_작업순서\\input.txt','r')
T = 1
for test_case in range(1,T+1):
    totalnode , N = map(int,input().split())
    totallist = list(map(int, input().split()))
    newlist = [(totallist[idx],totallist[idx+1]) for idx in range(len(totallist)-1) if idx % 2 == 0] # 간선의 정보를 둘씩 나눠서 튜플로 저장
    newlist = sorted(newlist,key = lambda x : x[1]) # 자식을 기준으로 간선을 정렬
    adjlist = [[] for _ in range(totalnode)] # 간선의 정보를 새로 저장할 2차원 배열
    for tups in newlist:
        adjlist[tups[1]-1].append(tups[0]) # 리스트의 n번째칸에는 n의 부모들의 목록이 적혀있다.  
    rst = []
    while len(rst) < totalnode: # 정답이 완성될때까지 반복
        for idx in range(len(adjlist)): 
            if adjlist[idx] == []: #부모가없는 친구들먼저 처리
                rst.append(idx+1)
                adjlist[idx].append(0) # 중복방지를위해 0으로 매꿔둠
                for jdx in range(len(adjlist)): 
                    if idx+1 in adjlist[jdx]: # 처리된친구가 부모였던친구들은 부모목록에서 정리
                        adjlist[jdx].remove(idx+1)
                    
    print('#',end='')
    print(test_case, end=' ')
    print(*rst) # 출력
    
        