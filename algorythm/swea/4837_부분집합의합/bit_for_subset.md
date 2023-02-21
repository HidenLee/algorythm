# 비트연산자로 부분집합 구하기

## 준비물

```python
arr = ['fish','and','chips']
N = len(arr)

for i in range(1<<N):
  # j: arr의 idx
  for j in range(N):
  if i & (1<<j):
    print(arr[j], end=' ')
  print()
```

## 1<<2 의 의미

```python
N = 3
print(1<<N) # 8
```