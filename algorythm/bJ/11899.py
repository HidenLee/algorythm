# https://www.acmicpc.net/problem/11899

left = 0
right = 0

for b in input():
    if b == ")":
        if right:
            right -= 1
        else:
            left += 1
    else:
        right += 1
print(right+left)