import re
import random
import time

a = 'This is goof.'
b = random.random()
c = random.uniform(10,20)
print(b)
print(c)

def extendlist(val, list=[]):
    list.append(val)
    return list


# if __name__ == '__main__':
#
#     list1 = extendlist(10)
#     list2 = extendlist(123,[])
#     list3 = extendlist('a')
#
#     print(list1)
#     print(list2)
#     print(list3)



# def f1(lin):
#     l1 = sorted(lin)
#     l2 = [i for i in l1 if i <0.5]
#     return [i*i for i in l2]
#
#
# def f2(lin):
#     l1 = [i for i in lin if i <0.5]
#     l2 = sorted(lin)
#     return [i*i for i in l2]
#
#
# def f3(lin):
#     l1 = [i*i for i in lin]
#     l2 = sorted(l1)
#     return [i for i in l1 if i<(0.5*0.5)]
#
#
# if __name__ == '__main__':
#     import cProfile
#     lin = [random.random() for i in range(10000)]
#     cProfile.run('f1(lin)')
#     cProfile.run('f2(lin)')
#     cProfile.run('f3(lin)')


# 初始化__init__
class Hero(object):

    def __init__(self,shuxing):   # 实例化调用类时自动调用初始化方法
        self.sx = shuxing
        print('已经调用该方法')
        pass

    def __zdy__(self):
        print('自定义方法')
        pass

    def __del__(self):   # 该方法不定义也自动运行（在程序最后才进行销毁，如果自己定义使用该方法，可以在程序过程中删除），删除实例
        print('实例已经删除')

    def __zdy2__(self):
        print('自定义方法2')
        pass

# yu = Hero('hp')
#
#
# # del yu
# print(yu.sx)  # 已经被删除，报错未定义
# yu.__zdy__()  # 实例在此还未删除
# # 析构,销毁实例
# del yu
# print(yu.sx)  # 已经被删除，报错未定义
# yu.__zdy2__()   # 自定义方法2没法执行

# 继承
class Rec():
    # 定义一个长方形
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length*self.width
        return area
x1 = Rec(10,20)
print('----------')
print(x1.area())

class Sjc(Rec):
    '''继承长方形'''
    pass
# 调用继承的Sjc
x2 = Sjc(15,20)
print('----------')
print('已经继承长方形',x2.area())  # 继承类似浅复制，只是引用，没有复制变量空间

# 重写方法
class Sjc2(Rec):
    '''继承长方形'''
    def __init__(self,width): # 重写自定义方法
        self.length = width
        self.width =width

x3 = Sjc2(20)
print('----------')
print('1再次继承长方形',x3.area())

# 重写方法后+调用父类方法
class Sjc3(Rec):
    '''继承长方形'''
    def __init__(self,length,width): # 重写自定义方法
        if length == width:
            print('是正方形，调用父类方法')
            # Rec.__init__(self,length,width)  # 调用父类方法1
            super().__init__(length,width)   # 调用父类方法2，不需要self
        else:
            print('不是正方形，程序结束')

x4 = Sjc3(30,30)
print('----------')
print('2再次继承长方形',x4.area())
print('----------')
x5 = Sjc3(50,30)

# 找父类的方法
print(Sjc3.__base__)   # 查询继承的父类名称
print(Sjc3.__bases__)   # 查询继承的父类
print(Rec.__bases__)   # 查询继承的父类
