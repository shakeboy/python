import turtle                                   #导入模块.

#画正方体正面.
n = 100                            			#正方体边长.
turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.pencolor('red')                  		#画笔颜色为红色.
turtle.begin_fill()
turtle.fillcolor('red')                    	#填充颜色为红色.
for i in range(4):
  turtle.forward(n)
  turtle.left(90)
turtle.end_fill()
#画正方体顶面.
turtle.penup()
turtle.goto(-100,n-50)
turtle.pendown()
turtle.pencolor('green')                		#画笔颜色为绿色.
turtle.begin_fill()
turtle.fillcolor('green')                  	#填充颜色为绿色.
turtle.left(45)
turtle.forward(int(n * 0.6))             	#倾斜边长为60.
turtle.right(45)
turtle.forward(n)
turtle.left(360 - 135)
turtle.forward(int(n * 0.6))              	#倾斜边长为60.
turtle.end_fill()
#画正方体右侧面.
turtle.left(45)
turtle.penup()
turtle.goto(n-100,-50)
turtle.pendown()
turtle.pencolor('blue')                 		#画笔颜色为蓝色.
turtle.begin_fill()
turtle.fillcolor('blue')                  	#填充颜色为蓝色.
turtle.left(135)
turtle.forward(int(n * 0.6))              	#倾斜边长为60.
turtle.left(45)
turtle.forward(n)
turtle.left(135)
turtle.forward(int(n * 0.6))            	      #倾斜边长为60.
turtle.right(90)
turtle.end_fill()
turtle.done()
