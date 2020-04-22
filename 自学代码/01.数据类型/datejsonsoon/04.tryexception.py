# 异常捕捉
try:
    print(x)
except:
    print("An exception occurred")

# 异常类型捕捉
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# 如果没有引发错误，那么您可以使用 else 关键字来定义要执行的代码块：
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# raiseException
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
