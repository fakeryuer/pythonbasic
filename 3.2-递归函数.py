# 递归的含义：函数调用函数本身

# 重点：1、基线条件\ 2、循环条件

def factorial(n):
    if n == 1:      # 条件1
        return 1
    return factorial(n-1)*n     # 条件2

print(factorial(5))


print('------雪花绘制实例递归-------')
import turtle
def koch(size, n):
    if n == 0:      # 基线条件
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
           turtle.left(angle)
           koch(size/3, n-1)    # 循环条件
def main():
    # 初始化绘图
    turtle.speed(30)        # 绘制速度
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    # 递归参数
    level = 3      # 3阶科赫雪花，阶数   三角形》》雪花
    koch(400,level)     # 调用递归函数
    # 开始绘制，三段
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
    turtle.done
main()