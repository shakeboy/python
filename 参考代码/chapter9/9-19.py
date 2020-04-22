import shelve
with shelve.open('shelve_file') as shelve_file:
  print(shelve_file['tg'])   					#读数据.
  print(shelve_file.get('tj'))                         #读数据.
