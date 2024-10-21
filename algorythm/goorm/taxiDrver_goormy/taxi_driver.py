from collections import deque

def find_route(frx,fry,tox,toy):
	global arr
	visit = [[False]*N for _ in range(N)]
	delta = [(0,1),(1,0),(0,-1),(-1,0)]
	q = deque([(frx,fry,0)])
	while(q):
		ox,oy,d = q.popleft()
		if ox == tox and oy == toy:
			return d
		visit[oy][ox] = 1
		for dt in delta:
			nx, ny = ox+dt[0], oy+dt[1]
			if 0<=nx<N and 0<=ny<N and not visit[ny][nx] and arr[ny][nx] != 1:
				visit[ny][nx] = 1
				q.append((nx,ny,d+1))
	return 10e9


N, M = map(int,input().split())
X, Y, Z = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
now = []
for _ in range(M):
	a, b, c, d = map(int,input().split())
	nx, ny = a, b
	if now:
		nx, ny = now.pop()
	ans -= find_route(nx-1,ny-1,a-1,b-1)*Z
	dist = find_route(a-1,b-1,c-1,d-1)
	if dist > 5:
		ans += (dist-5)*Y
	ans += X - dist*Z
	now.append((c,d))
print(ans)