

class Hero():
    def __new__(cls, *args, **kwargs):      # new方法创建一个实例，@1 不进行实例的属性附加，创建后才能进行init初始化
        print('--01.1--new方法')
        print('--01.2--%s方法' % cls)
        # super().__new__(cls)               # 01 此时不能用super调用父类方法
        # 02 只能使用父类名称进行调用；03 必须使用该句，否则无法执行初始化
        return object.__new__(cls)

    def __init__(self):
        print('--02--初始化')              # @2 初始化才对实例进行属性附加


a = Hero()
b = Hero()
print(id(a))
print(id(b))    # id不同，不是单例


# 单例模式---节省内存，始终保持一个实例
# 利用new方法设置：
class Hero2():
    __attr = None   # __表示私有属性；定义判断是否实例化

    def __new__(cls, *args, **kwargs):
        if cls.__attr is None:      # 通过判断是否已经实例，进行第一次实例化
            cls.__attr = object.__new__(cls)
            return cls.__attr
        else:
            return cls.__attr       # 已经实例过，直接覆盖原实例，不再进行初始化

    def __init__(self, l, w):
        self.l = l
        self.w = w
        print('l的属性值为:%s' % l)
        print('初始化属性')


x1 = Hero2(123, 123)
x2 = Hero2(1234, 1234)
print(id(x1))
print(id(x2))
print(x1.l, x2.l)  # x1属性已经被覆盖
