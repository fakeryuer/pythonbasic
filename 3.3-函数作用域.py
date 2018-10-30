
a = 1

def f1():
    a = 2   # 局部变量
    print(a)

f1()

def f2():
    global a    # 全局变量
    a = 3
    print(a)

f2()


def f3():
    a = 100
    def f4():
        nonlocal a       # 该句将输出 100 》 200
        a = 200
    f4()
    print(a)


f3()