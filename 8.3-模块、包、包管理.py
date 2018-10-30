
# 导入模块时是根据那个路径作为基准来进行的呢？即：sys.path
import sys
print(sys.path)

'''
导入模块有一下几种方法：
import module
from module.xx.xx import xx
from module.xx.xx import xx as rename  
from module.xx.xx import *(或函数名)
'''

print(__name__)     # __name__这个内置变量值就是__main__

if __name__ == '__main__':      # 该语句可以控制代码在被其他模块导入时不被执行
    pass                         # 认为为了调试模块，在模块导入的时候并不执行if下面的语句。

print("this is before if __name__:%s"%__name__)
if __name__=='__main__':
    print("this is after if __name__:%s"%__name__)

'''
包，就是包含了很多模块的文件夹
    构造包：首先需要把py文件放入包中，并且加一个__init__.py文件
    通过包，我们加入了层级导入。
    相对路径导入:在包管理中，可以通过 . (一个点) 和 .. (两个点)分别来导入同层和上一层的模块

'''