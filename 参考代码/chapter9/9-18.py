import shelve
tg = dict(zip(['name','age'],['Tong Gang',31]))    #创建数据.
tj = dict(zip(['name','age'],['Tie Jin',42]))       #创建数据.
with shelve.open('shelve_file') as shelve_file:
  shelve_file['tg'] = tg                        #向文件中写入内容.
  shelve_file['tj'] = tj                        #向文件中写入内容.
  print("写入数据成功！")
