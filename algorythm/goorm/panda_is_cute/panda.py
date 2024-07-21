# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, M ,K = map(int,input().split())
pandas = []
xsum, ysum = (0,0)
for _ in range(K):
	ipt1, ipt2 = map(int, input().split())
	pandas.append((ipt1,ipt2))
	xsum += ipt2
	ysum += ipt1
cenx = xsum//K
ceny = ysum//K

delta = [(0,1),(1,0),(0,-1),(-1,0)]
from collections import deque
q = deque([(ceny,cenx)])
while(q):
	oy, ox = q.popleft()
	if (oy,ox) in pandas:
		for dty,dtx in delta:
			if 0 <= oy + dty < N and 0 <= ox +dtx < M:
				q.append((oy+dty,ox+dtx))
		continue
	ans = 0
	for py,px in pandas:
		ans += (py-oy)**2 + (px-ox)**2
	print(ans)
	break