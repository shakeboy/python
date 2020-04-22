#定义函数.
def stuInfo(sno,sname,age = 18):
  return "学号：" + sno + "," + "姓名：" + sname + "," + "年龄：" + str(age)
print(stuInfo(sname = "Rose",sno = "x1001"))              #age使用默认参数值18.
print(stuInfo(sname = "Mike",sno = "x1002",age = 20))   #age使用传入参数值20.
