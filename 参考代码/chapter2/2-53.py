import random

#字符集合.
str = "0123456789abcdefghijklmnopqrstuvwxyaABCDEFGHIJKLMNOPQRSTUVWXYZ"
len = str.__len__()             				#str中字符的个数.
yzm = ""
for i in range(4):
  yzm = yzm + str[random.randint(0,len-1)]    	#生成验证码.
print("当前验证码:",yzm)
yzmInput = input("请输入验证码: ")
if yzm == yzmInput:            					#验证码验证.
  print("验证通过！")
else:
  print("验证失败！")
