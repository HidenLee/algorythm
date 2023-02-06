'''
삼성시는 버스 노선을 일반, 급행, 광역 급행으로 구분해 새롭게 바꾸려고 한다. 모든 정류장은 1번부터 1000번까지의 번호가 부여되어 있으며, 각 노선은 A에서 B번 정류장까지 다음 규칙에 따라 운행한다.
- 모든 버스는 A번에서 출발해 B번까지 운행하므로, A와 B정류장에는 반드시 정차한다.
- 일반버스는 A번부터 B번 사이의 모든 정류장에 정차한다.
- 급행 버스는 A가 짝수인 경우 A와 B 사이의 모든 짝수 번호 정류장에 정차하고, A가 홀수인 경우 A와 B사이의 모든 홀수 번호 정류장에 정차한다.
- 광역 급행 버스는 A가 짝수인 경우 A와 B 사이의 모든 4의 배수 번호 정류장에, A가 홀수인 경우 A와 B 사이의 3의 배수이면서 10의 배수가 아닌 번호 정류장에 정차한다.
버스의 종류와 출발 도착 정류장에 대한 정보가 주어질 때, 최대 몇 개의 노선이 같은 정류장에 정차하는지 알아내는 프로그램을 만들어보자.

[입력]
첫 줄에 테스트케이스의 개수 T가 주어진다. (1<=T<=1000)
다음 줄부터 각 테스트케이스 별로 첫 줄에 노선의 수 N이 주어지고(1<=N<=100), N개의 줄에 걸쳐 버스 타입 (1 일반, 2 급행, 3 광역 급행)과 출발 정류장 번호 A, 종점인 정류장 번호 B가 빈칸으로 구분되어 주어진다. (1<=A

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.
'''
def func1(): # 각 종류의 버스가 여러대일때를 고려못함 다시짜자
    N = int(input())
    busdict = {}
    for roop in [1,2,3]:
        busdict[roop] = list(map(int,input().split()))
    buslist1 = list(range(busdict[1][0],busdict[1][1]+1))
    buslist2 = list(range(busdict[2][0],busdict[2][1]+1,2))
    if buslist3[2][0] % 2 == 0:
        buslist3 = list(range(4,1001,4))
    else:
        buslist3 = list(x for x in range(1,1001) if x % 3 == 0 and x % 10 != 0)
    rst = 0
    for busstop in range(1,1001):
        temp = buslist1.count(busstop) + buslist2.count(busstop) + buslist3.count(busstop)
        if rst < temp:
            rst = temp
    return rst

def func2(): # 새로 짜는 김에 이번엔 좀 더 효율적으로 해보자
    # 버스 리스트 작성
    N = int(input())
    buslist1 = [] 
    buslist2 = []
    buslist3 = []
    stoplist = range(1,1001) # 전체 정류소 목록
    rst = 0 # 
    for roop in range(N):
        ipt = list(map(int,input().split())) # 인풋값의 첫 요소가 1,2,3일때 나눠서 구분(유사 switch 코드)
        if ipt[0] == 1:
            buslist1.append(ipt[1:])
        elif ipt[0] == 2:
            buslist2.append(ipt[1:])
        elif ipt[0] == 3:
            buslist3.append(ipt[1:])
        else:
            pass


    stoplist1 = stoplist[:] # 일반 버스부터 정류소 카운팅        
    for bus in buslist1: 
        stoplist1 = [x for x in stoplist1 if bus[0] <= x and x <= bus[1]]
    if stoplist1 == []: # 혹시 겹치는게 있어..?
            rst += 1
    else:
        stoplist1 = stoplist[:]
    
    stoplist12 = stoplist1[:] # 급행 버스를 추가한 로직!
    for bus in buslist2:
        if bus[0] % 2 == 0:
            stoplist12 = [x for x in stoplist12 if x % 2 == 0 and bus[0] <= x and x <= bus[1]] 
        else:
            stoplist12 = [x for x in stoplist12 if x % 2 != 0 and bus[0] <= x and x <= bus[1]]
    if stoplist12 != []: # 혹시 겹치는게 있어..?
        rst += 1
    else:    
        stoplist12 = stoplist1[:]

    stoplist123 = stoplist12[:] #마지막으로 광역까지!
    for bus in buslist3:
        if bus[0] %2 == 0:
            stoplist123 = [x for x in stoplist123 if x % 4 == 0 and bus[0] <= x and x <= bus[1]]
        else:
            stoplist123 = [x for x in stoplist123 if x % 3 == 0 and x % 10 != 0 and bus[0] <= x and x <= bus[1]]
    if stoplist123 != []: # 혹시 겹치는게 있어...?
            rst += 1

    #일반은 안오는데 혹시 광역이랑 급행이 겹칠까봐!!
    stoplist23 = stoplist[:]
    for bus in buslist2:
        if bus[0] % 2 == 0:
            stoplist23 = [x for x in stoplist23 if x % 2 == 0 and bus[0] <= x and x <= bus[1]]
        else:
            stoplist23 = [x for x in stoplist23 if x % 2 != 0 and bus[0] <= x and x <= bus[1]]
    for bus in buslist3:
        if bus[0] %2 == 0:
            stoplist23 = [x for x in stoplist23 if x % 4 == 0 and bus[0] <= x and x <= bus[1]]
        else:
            stoplist23 = [x for x in stoplist23 if x % 3 == 0 and x % 10 != 0 and bus[0] <= x and x <= bus[1]]
    if stoplist23 != []: # 혹시 겹치는게 있어...?
            if rst !=3:
                rst = 2


    #급행은 안오는데 혹시 일반이랑 광역이 겹칠까봐!!
    stoplist13 = stoplist[:]
    for bus in buslist1:
        stoplist13 = [x for x in stoplist13 if bus[0] <= x and bus[0] <= x and x <= bus[1]]
    for bus in buslist3:
        if bus[0] % 2 == 0:
            stoplist13 = [x for x in stoplist13 if x % 4 == 0 and bus[0] <= x and x <= bus[1]]
        else:
            stoplist13 = [x for x in stoplist13 if x % 3 == 0 and x % 10 != 0 and bus[0] <= x and x <= bus[1]]
    if stoplist13 != []: # 혹시 겹치는게 있어...?
            if rst !=3:
                rst = 2
    return rst

def func3(): # func2는 효율만 생가하다가 같은 종류의 버스가 같은 정류소에 들릴때 카운트를 안했다 func3은 이를 보완한 코드
    N = int(input())
    buslist = []
    rst = 0
    for roop in range(N):
        ipt = list(map(int,input().split())) # 인풋값의 첫 요소가 1,2,3일때 나눠서 구분(유사 switch 코드)
        if ipt[0] == 1:
            buslist.append([x for x in range(1,1001) if ipt[1] <= x and x <= ipt[2]])
        elif ipt[0] == 2:
            if ipt[1] % 2 ==0:
                buslist.append([x for x in range(1,1001) if x % 2 == 0 and ipt[1] <= x and x <= ipt[2]])
            else:
                buslist.append([x for x in range(1,1001) if x % 2 !=0 and ipt[1] <= x and x <= ipt[2]])
        elif ipt[0] == 3:
            if ipt[1] % 2 == 0:
                buslist.append([x for x in range(1,1001) if x % 4 == 0 and ipt[1] <= x and x <= ipt[2]])
                if ipt[1] % 4 != 0:
                    buslist[-1].insert(0,ipt[1])
            else:
                buslist.append([x for x in range(1,1001) if x % 3 == 0 and x % 10 != 0 and ipt[1] <= x and x <= ipt[2]])
                if ipt[1] % 3 !=0:
                    buslist[-1].insert(0,ipt[1])
                    
                elif ipt[1] % 10 == 0:
                    buslist[-1].insert(0,ipt[1])
    temp = 0                    
    for stop in range(1,1001):
        cnt = 0
        for bus in buslist:
            if stop in bus:
                cnt += 1
            if temp < cnt:
                temp = cnt
    return temp         
                



T = int(input())
for test_case in range(1,T+1):
    print(f'#{test_case} {func3()}')
