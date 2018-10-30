'''
什么叫描述符？
描述符协议：python描述符是一个“绑定行为”的对象属性，
在描述符协议中，它可以通过方法重写属性的访问。
这些方法有__get__(), __set__(), 和__delete__()。
如果这些方法中的任何一个被定义在一个对象中，这个对象就是一个描述符。
用代码进行实例解释：
'''

class Myclass():
    def __get__(self, instance, owner):
        print('使用了Myclass的get方法')

    def __set__(self, instance, value):
        print('使用了Myclass的set方法')

    def __delete__(self, instance):
        print('使用了Myclass的delete方法')


class Youclass():
    x = Myclass()           # 类中调用了其他类的方法，也算是YOUCLASS的属性，x 称为描述符


y = Youclass()
y.x              # ——get方法
y.x = 1234      # 重新赋值——set方法
del y.x         # 删除——delete方法