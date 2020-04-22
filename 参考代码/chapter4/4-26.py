LSZ_dict = {"姓名":"李时珍","出生时间":1518,"籍贯":"湖北","职业":"医生"}
print("字典中所有的键 / 值:",end = '')
for key,value in LSZ_dict.items():
  print(key,'/',value,end = ', ')
print()
print("字典中所有的键:",end = '')
for key in LSZ_dict.keys():
  print(key,end = ', ')
print()
print("字典中所有的值:",end = '')
for value in LSZ_dict.values():
  print(value,end = ', ')
