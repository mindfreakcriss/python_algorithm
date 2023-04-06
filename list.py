#coding-utf-8

list1 = [1,2,3,4,5]

#index
print("list1[0] = ", list1[0])
#slice
print("list1[1:4] = " , list1[1:4])
#append
list1.append(6)
print("list1 = ", list1)
#delete
del list1[5]
print(list1)

# 操作符号
# 长度
length = len(list1)
print("list1 的长度为 ：" , length)

# 组合
list2 = [1,2,3] + [3,4,5]
print(list2)

#重复
list3 = ["hi"] * 4
print(list3)

#是否在里面
a = 3 in list1

print(a)

#迭代
for x in list1:
    print(x)

list1.insert(2,10)

print(list1)

#反向
list1.reverse()
print(list1)