'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

[입력]
첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
 
[출력]
#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.
'''

T = int(input()) # 노선의 수

for lane in range(1,T+1):
    K, N, M = tuple(map(int,input().split())) # K는 한번에 이동가능한 최대 거리, N은 목적지까지 거리, M은 충전기의 갯수
    chargerindex = list(map(int,input().split())) # 충전기의 위치, 인덱스0이 출발선이라고 가정하면 받은 변수값 그대로 인덱스로 사용해도 무방
    chargerindex.insert(0,0) # 출발지도 충전함으로 추가
    validate_lane = True # 목적지에 도착 가능할지 확인할 bool값
    for idx in range(M): 
        if chargerindex[idx] + K < chargerindex[idx+1]: #한 정류소에서 다음정류소까지 도달 못한다면 아웃
            validate_lane = False
            break
    else:
        if chargerindex[-1] + K < N: # 마지막 정류소에서 목적지까지 갈 수 없다면 아웃
            validate_lane = False
        else: # 최솟값 찾기는 여기 부터!
            ablelist = [] # 목적지에 도달 가능한 각 시행에서 정차 횟수 기록할 리스트
            start = chargerindex[0] # 출발점은 0
            cnt = 0 #도달까지 걸린 횟수 측정
            while start < N-K: # 도착점에 도달하기 직전에 루프 탈출
                templist = [x for x in chargerindex if x <= start + K] #리스트컴프리헨션, 임시리스트에는 버스가 최대한 멀리갔을때 지나쳤을 정류소들의 목록이 들어감 
                start = templist[-1] # 그 목록에서 가장 나중의 원소를 출발점으로 바꾸고 다시 반복, 가장 멀리있는 충전소만 점프점프해서 간다는게 이 로직의 핵심
                cnt += 1 # 반복 회수 측정
    if validate_lane == False: # 앞에서 도달할수 없는 경우란게 밝혀졌다면 0을 출력
        print(f'#{lane} 0')
    else:
        print(f'#{lane} {cnt}')
