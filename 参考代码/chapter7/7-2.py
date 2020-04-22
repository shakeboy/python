import turtle
t = turtle.Turtle()               	#创建turtle对象
t.penup()
t.goto(-80,20)
t.write("    望庐山瀑布",font=("微软雅黑",14,"normal"))	#设置字体、大小、加粗.
t.sety(-10)                    		#画笔向下移动到-10.
t.write("日照香炉生紫烟",font=("微软雅黑",14,"normal"))
t.sety(-40)                    		#画笔向下移动到-40.
t.write("遥看瀑布挂前川",font=("微软雅黑",14,"normal"))
t.sety(-70)                    		#画笔向下移动到到-70.
t.write("飞流直下三千尺",font=("微软雅黑",14,"normal"))
t.sety(-100)                   		#画笔向下移动到到-100.
t.write("疑是银河落九天",font=("微软雅黑",14,"normal"))
t.hideturtle()
turtle.done()
