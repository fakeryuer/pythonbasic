# 创建生成器2种方法
g = (x for x in range(10))  # mtod 1
print(next(g))
print(next(g))
print(next(g))

def func(n):
    a = 0
    while a<n:
        yield a
        a += 1


ge = func(10)
print(next(ge))
print(next(ge))
print(next(ge))
'''
注意：yield 表达式只能在函数中使用,在函数体中使用 yield 表达式可以使函数成为一个生成器；
yield 可以返回表达式结果，并且暂定函数执行,直到next激活下一个yield

Python使用生成器对延迟操作提供了支持。所谓延迟操作，是指在需要的时候才
产生结果，而不是立即产生结果,从而节省大量的空间,这也是生成器的主要好处
'''


# 所有的生成器都是迭代器；迭代器不一定是生成器
'''
可迭代对象与迭代器：
from collections import Iterable ,Iterator

~可迭代对象: Iterable     
1 可迭代对象能用for循环进行遍历
2 可以使用 isinstance() 判断一个对象是否是 Iterable 对象。

~迭代器： Iterator    
1 迭代器不仅可以通过for进一行遍历，可以通过next取值
2 可以使用 isinstance() 判断个对象是否是 Iterator ：
'''

from collections import Iterable ,Iterator


list1 = [i for i in range(10)]
tu1 = (1,2,3,4,5,6)
st1 = 'i hate you'
# 可迭代对象判断：isinstance 返回bool值
print(isinstance(list1,Iterable))
print(isinstance(tu1,Iterable))
print(isinstance(st1,Iterable))
# 迭代器对象判断
print(isinstance(list1,Iterator))
print(isinstance(tu1,Iterator))
print(isinstance(st1,Iterator))

# 从可迭代对象生成一个迭代器： 迭代器=iter(可迭代对象)
print('-----可迭代对象变成迭代器-----')
ilist = iter(list1)
itu = iter(tu1)
ist = iter(st1)
print(isinstance(ilist,Iterator))
print(isinstance(itu,Iterator))
print(isinstance(ist,Iterator))


'''
迭代器对象本身需要支持以下两种方法，它们一起构成迭代器协议：
iterator.__iter__()
iterator.__next__()
扩展提示：通过定义__iter__和__next__方法，以自定义迭代器
-------------------------------------------------
取值：
next(iterator)
iterator.__next__()
注意：如果迭代器值取完之后，会返回 StopIteration 错误
'''

# 斐波那契数列
def fbnq(n):
    x = 0
    x1 = 1
    x2 = 1
    if n == 0 or n == 1:
        yield ('第%s相数为%s' %n)
    elif n < 0:
        yield('请输入一个正整数')
    else:
        for i in range(1,n):
            x = x1 + x2
            x1 = x2
            x2 = x
            yield('第%i项数为%s' %(i+1,x))



y = fbnq(5)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
