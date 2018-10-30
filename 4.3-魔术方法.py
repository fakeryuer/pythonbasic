# 魔术方法是满足特定条件‘自己触发’的，是python自带的，无法自己定义
# 自定义一个字符串拼接方法

class Add(object):
    def __init__(self,str1):
        self.str1 = str1

    def __add__(self, other):       # add 魔术方法在使用 + 时调用的
        sum = self.str1 + other.str1
        return  sum

a = Add('abcd123')
b = Add('EFGH456')
print(a+b)

'''
运算符 魔术方法
__add__(self,other)	# x+y
__sub__(self,other)	# x-y
__mul__(self,other)	# x*y
__mod__(self,other)	# x%y
__iadd__(self,other)	# x+=y
__isub__(self,other)	# x-=y
__radd__(self,other)	# y+x
__rsub__(self,other)	# y-x
__imul__(self,other)	# x*=y
__imod__(self,other)	# x%=y
'''


# 常用的魔术方法
class Abc(object):
    """文档说明：使用doc方法进行调用查看"""

    def __init__(self,zfc):
        self.zfc = zfc

    def __str__(self):
        return '面对用户的简介信息：str方法\n=========='

    def __repr__(self):

        return  '交互模式面对开发者的创建时详细信息：repr方法\n=========='

    def __call__(self, *args, **kwargs):
        print('使用call能使实例像函数一样能被调用')

a = Abc('asd')
print(a)               # 如果对象没有定义__str__方法，则调用__repr__方法；
                      # print时先调用str方法，如果str未定义，则使用repr方法
                    #   交互模式，输入对象，返回repr
a()                 # call方法进行函数调用
print(a.__doc__)
print(a.__dict__)    #dict查看所有的属性
