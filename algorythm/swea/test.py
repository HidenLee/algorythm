arr = ['Fish', 'And', 'Chips']
N = len(arr)

# arr에 대한 모든 경우의 수
for i in range(1 << N):
	# j : arr의 index
	for j in range(N):
		if i & (1 << j):
			print(arr[j], end=' ')
	print()