import sys
sys.stdin = open('input.txt','r')

def check_side(ladder, row, col):
    # direction == -1: 왼쪽, +1: 오른쪽
    for direction in range(-1, 2):
        if direction == 0:
            continue
        side_col = col + direction
        if 100 > side_col >= 0:  # 옆이 인덱스 범위 내에 있고
            if ladder[row][side_col] == 1:  # 갈 수 있으면
                return direction  # 해당 방향 리턴
    return 0


def can_go_down(ladder, row, col):
    down_row = row + 1  # 한 줄 아래로
    if 100 > down_row >= 0:  # 인덱스 범위 내에 있고
        if ladder[down_row][col] == 1:  # 길이 있으면
            return True
    return False


# f = open("./Python/im/from_notion/1210.txt", "r")
for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # tc = int(f.readline())
    # ladder = [
    #     list(map(int, f.readline().split())) for _ in range(100)
    # ]

    # 가능한 시작점 리스트
    starts = []
    for i in range(len(ladder[0])):
        if ladder[0][i] == 1:
            starts.append(i)
    # 최소값, 정답 변수
    mn = 2147483647
    answer = 0
    for col in starts:  # 시작점 리스트를 순회하며
        row = 0  # 시작 row
        start_col = col  # 시작 col 저장 변수
        distance = 0  # 거리 계산
        while row != 99:
            if distance > mn:  # 반복 중 거리가 최소값보다 크면 의미 없으므로 break
                break
            direction = check_side(ladder, row, col)  # 옆길 확인
            if direction:  # 옆에 길이 있으면, -1: 왼쪽, +1: 오른쪽
                col += direction  # 일단 옆으로
                distance += 1  # 이동거리추가
                while not can_go_down(
                    ladder, row, col
                ):  # 아래으로 갈 수 없으면
                    col += direction  # 옆으로
                    distance += 1  # 이동거리추가
                row += 1  # 앞으로 갈 수 있게 되면 한칸 아래로
                distance += 1  # 이동거리추가
            else:  # 옆에 길이 없으면
                row += 1  # 아래로
                distance += 1  # 이동거리추가
            if tc == 4 and start_col == 5:
                print(col,row,distance)    
        if distance < mn:  # 최소값 갱신
            mn = distance
            answer = start_col  # 해당 최소값일 때 시작 col을 answer에 저장
        # print(f"#{tc} {mn} {answer}")