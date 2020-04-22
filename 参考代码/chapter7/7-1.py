import turtle                                   #导入模块.
turtle.penup()
turtle.goto(-150,0)
turtle.pendown()
turtle.pencolor('blue')                  	#画笔颜色为蓝色.
turtle.begin_fill()
turtle.fillcolor('blue')                   	#填充颜色为蓝色.
for i in range(4):
  turtle.forward(100)                          #画笔向当前方向移动距离100.
  turtle.left(90)                               #画笔逆时针旋转90度。
turtle.end_fill()
#画圆.
turtle.penup()
turtle.goto(100,0)                             #将画笔移动到指定的绝对坐标位置(100,0)
turtle.pendown()
turtle.color('red')                      		#画笔颜色为红色.
turtle.pensize(3)                      		#画笔宽度为3.
turtle.circle(50)                       		#圆的半径为50.
turtle.done()                                   #使绘图容器不消失.