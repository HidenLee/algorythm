N, M, K = map(int, input().split())
pandas = []
for _ in range(K):
    ipt1, ipt2 = map(int, input().split())
    pandas.append((ipt1-1, ipt2-1))


# 최적의 점을 찾기 위해 거리의 제곱합을 최소화하는 점을 찾음
min_distance_sum = 10e9

# 주어진 점들을 제외한 모든 가능한 점들을 탐색
for y in range(N):
	for x in range(M):
		if (y, x) not in pandas:
			distance_sum = 0
			for py, px in pandas:
				distance_sum += (py - y) ** 2 + (px - x) ** 2
			else:
				min_distance_sum = min(min_distance_sum,distance_sum)
if min_distance_sum == 10e9:
	print(0)
else:
	print(min_distance_sum)
