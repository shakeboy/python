total = 0; ave = 0; count = 0
score = int(input("请输入学生英语成绩："))    #从键盘输入学生英语成绩.
while score != -1:         				#输入"-1"，结束录入.
  total = total + score     				#计算学生英语成绩总分.
  count = count + 1                            #计算录入成绩的学生数.
  score = int(input("请输入学生英语成绩："))	#从键盘输入学生英语成绩.
ave = total / count        				#计算学生英语成绩平均分.
print("录入学生英语成绩 %d 份, 学生英语总成绩 %d, 平均成绩 %4.2f."%(count,total,ave))
