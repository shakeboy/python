str = ["好雨知时节，当春乃发生。\n","随风潜入夜，润物细无声。"]
with open("杜甫.txt","w") as fp:
  fp.writelines(str)
  print("写入字符串序列成功！")
