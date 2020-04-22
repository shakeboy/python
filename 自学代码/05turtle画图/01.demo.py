import turtle
# 画布(Canvas) ：    画布是Turtle模块展开用于绘图的区域。我们可以设置它的大小和初始位置。
# 1.Turtle 库是 Python 语言中一个很流行的绘制图像的函数库
# Turtle 库用于绘制线、圆、其他形状或者文本
# 显示小乌龟的爬行轨迹，初始小乌龟在(0, 0)，前进方向为 x 轴正方向
# 绘制圆形
import turtle
turtle.color('red')
turtle.circle(39)


turtle.color('orange')
turtle.pensize(3)
turtle.circle(75)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(100)

turtle.color('purple')

for i in range(10):
  turtle.circle(i*10)
  turtle.left(126)
turtle.done()


