
#준혁님코드 각 출발점에서의 탐색이 다음 출발점에서의 탐색에 영향을 줌
for t in range(1, 2):
    test_case_number = int(input())
    world = [] #100*100의 2차원 배열
    for w in range(100):
        world.append(list(map(int, input().split())))

    start_point = list() #스타팅포인트들의 가로인덱스가 저장될 리스트
    for s in range(100): #스타팅포인트 100곳 중 1인곳들이 진짜 스타팅
        if world[0][s] == 1:
            start_point.append(s)
    print(start_point)
    for ans in start_point: #스타팅포인트 하나씩 밑으로 내려가기 시작!!
        i = ans #답은 스타팅포인트 ans를 출력해야 하므로 그때그때 바뀌는 x좌표 i를 만들어주자
        h = 0 # 높이 0에서 시작
        loc_now = [i, h] #현재 위치
        while h != 99: #높이 99면 멈춰야함
            if i == 0: #왼쪽 끝에 있다면
                if world[h][i + 1] == 1:  # 오른쪽으로 갈 수 있다면
                    loc_now = [i + 1, h]
                    world[h][i] = 0  # 이전 위치로 다시 돌아가지 않게 0을 넣어줌
                    i += 1
                else:  # 좌우 둘다 갈데 없다면 아래로 한칸
                    loc_now = [i, h + 1]
                    h += 1

            elif i == 99: #오른쪽 끝에 있다면
                if world[h][i - 1] == 1:  # 왼쪽으로 갈수 있다면
                    loc_now = [i - 1, h]  # 현재위치를 한칸 왼쪽으로 바꿔주고
                    world[h][i] = 0  # 이전 위치로 다시 돌아가지 않게 0을 넣어줌
                    i -= 1  # 진짜 i값도 바꿔줌
                else:  # 좌우 둘다 갈데 없다면 아래로 한칸
                    loc_now = [i, h + 1]
                    h += 1

            else: #가운데 어딘가에 있다면
                if world[h][i-1] == 1: #왼쪽으로 갈수 있다면
                    loc_now = [i-1, h ] #현재위치를 한칸 왼쪽으로 바꿔주고
                    world[h][i] = 0 #이전 위치로 다시 돌아가지 않게 0을 넣어줌
                    i -= 1 #진짜 i값도 바꿔줌
                elif world[h][i+1] == 1: #오른쪽으로 갈 수 있다면
                    loc_now = [i+1, h]
                    world[h][i] = 0 #이전 위치로 다시 돌아가지 않게 0을 넣어줌
                    i += 1
                else : #좌우 둘다 갈데 없다면 아래로 한칸
                    loc_now = [i, h+1]
                    h += 1

        if world[h][i] == 2: #골인이라면
            print(ans, t)
        else : #골인이 아니라면
            pass