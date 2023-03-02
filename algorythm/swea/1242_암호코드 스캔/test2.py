a = [1,2,3,4,5]
binrow = list(range(168))
idx = 21
n =3

print(a[-6])
# print(a[-len(a):][1])
# print(len(binrow),len(binrow[-168:]))
# print(binrow[-168:][0],binrow[-168:][167])

# for x in range(168):
#     if not x % n:
#         print(binrow[-168:][x])

# temp = ([binrow[-168:][x] for x in list(range(168)) if not x % n])
# temp = ''.join([a[-idx*8:][x] for x in range(idx*8) if not x % n])