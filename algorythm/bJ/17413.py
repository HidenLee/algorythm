# https://www.acmicpc.net/problem/17413


def generator(str1):
    i = 0
    N = len(str1)
    while i < N:
        if str1[i] == "<":
            tag_end_index = str1.find(">",i)
            yield str1[i:tag_end_index+1]
            i = tag_end_index + 1
        elif str1[i] == " ":
            yield str1[i]
            i += 1
        else:
            piece_start_index = i
            while i < N and not str1[i] in [" ","<",">"]:
                i += 1
            yield str1[piece_start_index:i][::-1]
print("".join(generator(input())))


# flag = False
# ipt = input()
# ans = ""
# temp = ""
# part = ""


# for elm in list(ipt):
#     if elm == "<":
#         flag = True
#         ans += part
#         part = ""
#     elif elm == ">":
#         flag = False
#         part = "<" + part + ">"
#         ans += part
#         part = ""
#     else:
#         if elm == " ":
#             ans += part +  " "
#             part = ""
#             continue
#         if flag:
#             part += elm
#         else:
#             part = elm + part
# print(ans.strip()+ " " + part)