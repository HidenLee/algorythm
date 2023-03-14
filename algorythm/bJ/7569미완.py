delta = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def findmax(arr):
    if not 0 in sum(arr,[]):
        return 0
    for i in range(M):
        for j in range(N*H):
            while True:
                nx = i
                nz, ny = divmod(j,N)
                for dlt in delta:
                    nx, ny, nz = nx+dlt[0], ny+dlt[1], nz+dlt[2]
                    if not arr[ny+nz*N][nx]:
                        pass






M, N, H = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(N*H)]
findmax(array)