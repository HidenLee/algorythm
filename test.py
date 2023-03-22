i,j,h = 3,39,512
k=[(a,b,c) for a in [i-1,i,i+1] for b in [j-1,j,j+1] for c in [h-1,h,h+1]]
print(k,len(k))
print(bool(-1))