N, M, x = map(int,input().split())
x -= 1
trees = list(map(int,input().split()))
_ = input()
time_passed = 0
ans = 0
for elm in list(input().split()):
	if trees[x] + time_passed >= M:
		ans += trees[x] + time_passed
		# trees[x] = max()
		trees[x] = -time_passed
	if elm == "R":
		x = x+1
		if x == N:
			x = 0
	if elm == "L":
		x = x-1
		if x == -1:
			x = N -1
	time_passed += 1
print(ans)				 