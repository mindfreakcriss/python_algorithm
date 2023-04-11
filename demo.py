# coding=utf-8

s = [9, 7, 8, 3, 2, 1, 5, 6]

length = len(s)

temp = []

for i in range(length):
    if s[i] % 2 == 0:
        temp.append(s[i] * s[i])
    else:
        temp.append(s[i])


print("变换前 %", s)
print("变换后 %", temp)