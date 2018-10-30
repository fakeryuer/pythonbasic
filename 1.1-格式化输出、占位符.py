print('--------------通用%-----------------')
'''
格式符
格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:
%s    字符串 (采用str()的显示)
%r    字符串 (采用repr()的显示)
%c    单个字符
%b    二进制整数
%d    十进制整数
%i    十进制整数
%o    八进制整数
%x    十六进制整数
%e    指数 (基底写为e)
%E    指数 (基底写为E)
%f    浮点数
%F    浮点数，与上相同
%g    指数(e)或浮点数 (根据显示长度)
%G    指数(E)或浮点数 (根据显示长度)
 
%%    字符"%"

---------------------
可以用如下的方式，对格式进行进一步的控制：
%[(name)][flags][width].[precision]typecode
(name)为命名
flags可以有+,-,' '或0。
    +表示右对齐。 默认右对齐省略+；+表示正号
    -表示左对齐。
    ' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。
    0表示使用0填充。
width表示显示宽度
precision表示小数点后精度
 
比如：

input = '{"a" : %s, "b" : "%s", "c": "1"}'  % (1234, 14289)

'''
print("%+10x" % 10)
print("%04d" % 5)
print("%6.3f" % 2.3)
print("%-6.3f" % 2.3)
print("%+6.3f" % 2.3)

# 上面的width, precision为两个整数。我们可以利用*，来动态代入这两个量。比如：

print("%.*f" % (4, 1.2))    # Python实际上用4来替换*。所以实际的模板为"%.4f"。

print('%+-6.3f' %10.3)   #显示正负

print('--------------format|python专有-----------------')
'''
函数 str.format()，增强了字符串格式化的功能。 
基本语法是通过 {} 和 : 来代替以前的 % 。 
format 函数可以接受不限个数参数，位置可以不按顺序。 
'''
'{:.2f}'.format(123.456)        # 保留2位小数
'{a:.2f}'.format(a=123.456)     # 参数格式
'{:.2%}'.format(123.456)    # 百分百

'{:0<10}'.format(123.456)    # 右对齐，用0填充
'{:1>10}'.format(123.456)    # 左对齐，用1填充
'{:2^10}'.format(123.456)    # 两端对齐，用1填充

# 位置
'{{  hello {0}  }}'.format('python')    # '{  hello python  }'
"{} {}".format("hello", "world")        # 不设置指定位置，按默认顺序'hello world'
"{0} {1}".format("hello", "world")     # 设置指定位置'hello world'
"{1} {0} {1}".format("hello", "world") # 设置指定位置'world hello world'

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))    # *表示列表，**表示字典
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0、1" 是可选的

print('网站：{}，地址：{}'.format(*my_list))