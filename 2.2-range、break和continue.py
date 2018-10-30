list1 = [1,23,4,5,34,44,44,45,6,43,6,3]

# for i in range(1,len(list1)):
#     print(list1[-i])

for j in list1:
    if j == 44:
        # break       # 停止函数
        continue     # 跳过此次循环
    else:
        print(j)


