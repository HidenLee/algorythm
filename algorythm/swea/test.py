N = int(input())    # N X N arr
arr = [list(map(int, input())) for _ in range(N)]   # 2d arr
s = 0
visited = [[0] * N for _ in range(N)]   # 방문 기록도 2차원으로 담기
'''
13101
10101
10101
10101
10021
시작점 2 -> dfs(2)
'''
def dfs(v, w):
    global s
    if s==1:
        return
    else:
        visited[v][w] = 1   # 방문 기록 찍기
        # print((v, w), end= '')   # 방문 기록 찍어보기

        # for i in range(v-1, v+2):
        #     for j in range(w-1, w+2):
        for i, j in [[v, w-1], [v+1, w], [v, w+1], [v-1, w]]:
            if 0 <= i < N and 0 <= j < N:
                # print(arr)

                if arr[i][j] == 3:
                    print(1)
                    s = 1

                elif arr[i][j] == 0 and visited[i][j] == 0:
                    dfs(i, j)
                    print(i, j)



dfs(4, 3)