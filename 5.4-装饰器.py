# 装饰器理解的前提1：闭包
def f1(func):
    # print(func)
    def f2():
        print('---闭包内进行功能扩展的函数---')
    return f2

# 装饰器理解的前题2：函数再定义改变指向（覆盖）； 函数可以当作其他函数参数传入
def f3(x):
    print('----%s次测试----' %x)


# f3 = lambda x:x*2
f3(0)
print(f3(1))
f1(f3(2))       # 函数可以当作其他函数参数传入


print('---------------------')
'''
什么是装饰器？
不更改原来函数的基础上，对原来的函数增加功能；
原理：函数当作参数传递到其他函数中；
符合开放封闭原则：
（对于已经实现功能的程序，不建议进行内部修改，防止其他程序错误；可以进行扩展开发；）
'''


def sin(x):

    def yz():       # 拓展的验证功能
        print('登陆验证')
        x()
    return yz


@sin    # 等价于sinup = sin(sinup)
def sinup():
    print('正在登陆')


sin(sinup())
# sin(sinup)()
sinup()   # 使用@之后，该句等价于sin(sinup)()