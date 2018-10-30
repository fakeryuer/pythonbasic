import copy

list1 = [1,2,3,4,5]
list2 = list1           # 浅复制只是引用变量空间
print('变量空间',id(list1))
print('复制后id',id(list2))

list3 = copy.deepcopy(list1)
print('深度复制后',id(list3))


print('--------1---------')
# 编码
a1 = '帅气的鱼'.encode(encoding='utf-8')    # 国际通用，包含世界上所有语言
a2 = '帅气的鱼'.encode(encoding='gbk')      # 国内标准，简略一些
print(a1)
print(a2)

# 解码
b2 = b'\xe5\xb8\x85\xe6\xb0\x94\xe7\x9a\x84\xe9\xb1\xbc'.decode('utf-8')
print(b2)

print('--------2---------')
# byte、bytearray 序列类型
c1 = bytes(b'abcd')     # 二进制序列类型
print(c1[0],c1[1],c1[2],c1[3])  # 输出ASCII码

c2 = bytearray(b'abcd')     # 区别是可以通过索引进行更改，byte无法更改
c2[0] = 98
print(c2[0],c2[1],c1[2],c2[3])