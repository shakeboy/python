a = 100
try:
  b = a + "python"
except Exception as e:
  print("异常类型: %s"%type(e))
  print("异常信息: %s"%e)
