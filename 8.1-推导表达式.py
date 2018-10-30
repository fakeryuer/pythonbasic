# 1列表推导式
# 推导+判断
l1 = [i for i in range(1,10) if i%2 == 0]
print(l1)
# 推导+三目运算
l2 = [i*2 if i%2 == 0 else 1 for i in range(1,10)]
print(l2)

# 2集合推导式
set1 = {i for i in range(1,10)}
print(set1)

# 3字典推导
dict1 = {i:j for i,j in enumerate('abcdefg')}      # enmuerate取下标和值
print(dict1)

# 元组推导式
tup1 = (i for i in range(10,20))
print(tup1)     # 返回一个生成器