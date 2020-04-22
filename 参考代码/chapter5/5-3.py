#定义函数.
def echelonArea(top,bottom,height):    	#3个形参:top上底,bottom下底,height高.
   area = 1 / 2 * (top + bottom) * height	#计算梯形面积.
   return area
if __name__ == "__main__":
   t = 3.6; b = 6.2; h = 4.5
   area1 = echelonArea(t,b,h)        		#方法一：调用函数，传入实参.
   print("area1 ＝",area1)
   area2 = echelonArea                      	#方法二：把函数对象赋给变量area2.
   print("area2 ＝",area2(t,b,h))
