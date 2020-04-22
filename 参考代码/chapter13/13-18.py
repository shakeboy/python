import multiprocessing,time,os,sqlite3,openpyxl

#创建/连接数据库.
def create_connect_database():
  try:
    conn = sqlite3.connect(os.getcwd()+'\\resources\\bookDB.db')
    cur = conn.cursor()
    cur.execute('''create table if not exists table_book(ID text PRIMARY KEY,Name 
text not null,Author text,Price float);''')
    conn.commit()
  except Exception as e:
    print("创建/连接数据库或创建数据表失败:",e)

#定义函数: 获取Excel文件的第1个工作表.
def eachXlsx(xlsxFn):
  wb = openpyxl.load_workbook(xlsxFn)
  ws = wb.worksheets[0]
  for index,row in enumerate(ws.rows):
    #忽略表头.
    if index == 0:
      continue
    yield tuple(map(lambda x:x.value,row))

#定义子进程调用函数.
def spFunc(filename):
  #连接数据库，将指定Excel文件中的数据导入数据库.
  with sqlite3.connect(os.getcwd()+'\\resources\\bookDB.db') as conn:
    try:
      cur = conn.cursor()
      sql = 'INSERT INTO table_book VALUES(?,?,?,?)'
      cur.executemany(sql,eachXlsx(filename))
      conn.commit()
    except Exception as e:
      print("导入数据失败.",e)

if __name__ == "__main__":
   print("excel文件数据导入数据库开始...")
   create_connect_database()                           #调用创建或连接数据库函数.
   pool = multiprocessing.Pool()                      #创建进程池.
   excel_path = os.getcwd() + "\\excel_files_dir" #Excel文件所在路径.
   excel_File_list = os.listdir(excel_path)         #Excel文件列表.
   #遍历Excel文件.每个进程负责将一个Excel文件中的书籍数据导入数据库.
   for filename in excel_File_list:
     excelFile = excel_path + "\\" + filename       #Excel文件及路径.
     pool.apply(spFunc,(excelFile,))
   pool.close()
   pool.join()
   print("Excel文件数据导入数据库结束！！！")
