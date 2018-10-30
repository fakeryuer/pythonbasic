class Base0(object):

    def f1(self):
        print('----base0---')


class A(Base0):
    def f1(self):
        print('----baseA1---')
        super().f1()  # 就近原则
    def fA(self):
        print('----baseA2---')


class B(Base0):
    def f1(self):
        print('----baseB1---')
    def fB(self):
        print('----baseB2---')


class C(A,B):
    def f1(self):
        print('----baseC1---')
        super().f1()

class D(B,A):
    pass

print(C.__bases__)  # 查看父类
print(D.__bases__)
c = C()
c.f1()
print(C.__mro__)  # 用这个方法查看多继承顺序
print('=======')
c.fA()
c.fB()


'''Mix-in 多继承设计模式
    --设计中一般只继承两层
'''