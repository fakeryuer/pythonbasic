'''
文件是否能自动关闭？
with open() 自动关闭
'''

with open('6-文件操作范例.txt','a+') as f:
    f.write('|我爱你，但是。。')
    f.seek(0)
    a = f.read()
    print(a)


# 上下文管理器
class Run():

    def __enter__(self):        # 可以用来对打开文件进行操作
        print('开始运行')
        return 'show time'

    def __exit__(self, exc_type, exc_val, exc_tb):      # 可以用来对关闭文件进行操作
        print('结束运行')


with Run() as a:    # a(可省略)接受返回值；可以在enter中用ruturn添加返回对象
    print(a)
    # 上下文管理：下方代码运行前使用enter方法，运行结束调用exit方法
    for i in range(10):
        print(i)