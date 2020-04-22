try:
  f = open("d:/test.txt","r")
  str = f.read()
except Exception as e:
  print("出现异常: %s"%e)
else:
  print('执行成功！')
finally:
  print("执行完毕！")
