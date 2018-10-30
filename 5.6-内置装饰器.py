'''
三种内置装饰器：
@property     >>>将类的一个方法变成属性
@classmethod  >>>标识类方法
@staticmethod >>>静态方法,def fun()中可以不写参数
'''


class Hero():

    def __init__(self, name, age, skill):
        self.name = name
        self.age = age
        self.skill = skill

    def qwer(self):
        print('%s使用了了%s技能' % (self.name, self.skill))

    @classmethod
    def move(cls):      # 1-cls参数
        print('使用了类方法 classmethod，将类的一个方法变成属性')

    @property
    def prty(self):     # 2
        print('使用了标识类方法 property，实例可以像使用属性一样被调用')

    @staticmethod
    def silent():       # 3-()可以不写参数
        print('staticmethod静态方法，不需要传递参数')


zed = Hero('zed', 23, 'QWER')
zed.qwer()

# classmethod
Hero.move()   # 不使用实例直接使用类的方法，没有@classmethod报错

# property
yasuo = Hero('yasuo', 28, 'QWER')
yasuo.prty      # 直接使用属性

# staticmethod
yasuo.silent()
