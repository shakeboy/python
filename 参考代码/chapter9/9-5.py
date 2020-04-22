mingTuple = ("王阳明","于谦","戚继光","海瑞","郑和","徐达") #明朝著名人物.
with open("Ming.txt","w") as fp:
  num = fp.write(str(mingTuple)) 			                #向文件中写入元组.
  print("写入元组成功！")
