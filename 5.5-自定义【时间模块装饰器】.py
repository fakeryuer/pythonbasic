import time

def run_time(func):     #计算程序运行时间
    def new_fun(*args,**kwargs):
        t0 = time.time()
        print('star time: %s'%(time.strftime('%x',time.localtime())) )
        back = func(*args,**kwargs)
        print('end time: %s'%(time.strftime('%x',time.localtime())) )
        print('run time: %s'%(time.time() - t0))
        return back
    return new_fun


@run_time
def myfun():
    list1 = [i for i in range(10000)]
    for j in list1:
        if j < len(list1)/2:
            print(j,end=',')
        elif j == len(list1)/2:
            print(j)
            print('\n')
        else:
            print(j, end=',')


myfun()