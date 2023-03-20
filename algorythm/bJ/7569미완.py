delta = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def findmax(arr):
    if not 0 in sum(sum(arr,[]),[]):
        return 0
    for h in range(H):
        for j in range(N):
            for i in range(M):
                stack=[(i,j,h)]
                while stack:
                    nx, ny, nz = stack.pop()
                    for dlt in delta:
                        nx, ny, nz = nx+dlt[0], ny+dlt[1], nz+dlt[2]
                        if arr[nz][ny][nx] != -1:
                            stack.append((nx,ny,nz))







M, N, H = map(int,input().split())
array = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
roaten = [[[0]*M for _ in range(N)] for _ in range(H)]
findmax(array)
