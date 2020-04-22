import shelve
with shelve.open('shelve_file') as shelve_file:
  tg = shelve_file['tg']                  #从文件中读取数据.
  tg['name'] = 'Tong Gen'                 #修改数据.
  shelve_file['tg'] = tg                  #存储数据.
  print(shelve_file ['tg'])
