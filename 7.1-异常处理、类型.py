# help(TypeError)  # 查看帮助
'''
代码错误，代码仍旧往下执行，不中断
'''
try:        # 写可能出现异常的代码
    class Hero():

        def __init__(self,name,age,skill):
            self.name = name
            self.age = age
            self.skill = skill

        def qwer(self):
            print('%s使用了了%s技能' %(self.name,self.skill))


    zed = Hero('zed',23,'QWER')
    zed.qwer()

except (TypeError,AssertionError) as e:     # 判断异常类型；不是这些类型错误，仍旧报错
    print('出现错误，运行此方案1')
except NameError:                                 # 可以有多个异常
    print('出现该类型错误，运行此方案2')
except Exception:                           # 不确定的异常；
    print('出现该类型错误，运行此方案3')
else:
    print('完美运行；无异常')
finally:
    print('无论是否有异常，运行此方案999')


print('-----------自定义异常-------------')
class Myerror(Exception):       # 所有异常都继承EXCEPTION
    pass

raise Myerror       # 只有主动抛出，才能执行自定义异常