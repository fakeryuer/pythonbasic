# 定制属性访问

class Hero():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getattr__(self, item):
        print('熟悉不存在，不调用我，则报错')

yu = Hero('yhy',20)

# 查找属性
print('查找属性----------')
print(hasattr(yu,'name'))  # 返回bool
yu.__getattribute__('age')   # 底层原理

# 得到属性
print('获取属性----------')
print(yu.name)      # mtod 1
print(getattr(yu,'name'))   # mtod 2
yu.__getattr__('name')  # mtod 3 两者相同，后者是底层原理

# 增加修改
print('增改属性----------')
print(yu.name)
setattr(yu,'name',999)      # 有则改
print(yu.name)

setattr(yu,'handsome',999)      # 无则增
yu.__setattr__('handsome',999)   # 底层原理
print(yu.handsome)

yu.nblity = 10000        #简单的增改mtod
print(yu.nblity)
# 删除属性
print('删除属性----------')
del yu.name     #简单mtod 1
# yu.__delattr__('name') # 底层原理
# print(yu.name)  # 报错，属性已经被删除