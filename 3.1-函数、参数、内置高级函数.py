def func1():        # 函数
    pass


def func2(a, *args, **kwargs):       # 不定长参数arg\kwargs
    pass


def func3(s, a=10, b= 20):       # 默认参数
    pass

# 高级函数
def is_odd(n):
    return n % 2 == 1

# map只返回T\F
new_list = list(map(is_odd, [1, 2, 3, 4, 5, 6, 7, 8]))
print('map返回',new_list)
# filter返回列表值
new_list = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8]))
print('filter返回',new_list)