import csv

#标题.
headers = ['NO','Name','Sex','Age','Salary']
#多行数据.
rows = [('1001','Jack','male',28,12800),('1002','Rose','female',22,8800),
                    ('1003','Tim','male','26',10800)]

#向csv文件中写数据.
try:
  #以写模式打开文件.
  with open('salary.csv','w',newline='') as file:
    fw = csv.writer(file)                           #返回writer对象.
    fw.writerow(headers)                            #向csv文件中写入一行数据.
    fw.writerows(rows)                               #向csv文件中写入多行数据.
    print('写入数据成功！')
except:
  print('写入数据失败！')

#从csv文件中读数据.
print('读取数据结果:')
try:
  #以读模式打开文件.
  with open('salary.csv','r') as file:
    fr = csv.reader(file)                             #返回reader对象.
    rows = [row for row in fr]                       #以列表形式返回fr中的数据.
    print("标题:",rows[0])
    print("第1行数据:",rows[1])
    column = [row[1] for row in rows]
    print("第1列数据:",column)
    print("第1行第1列数据:", rows[1][1])
except:
    print('读数据失败！')
