import os,sys,re

try:
  #获取目标文件夹的路径.
  source_file_dir = os.getcwd() + '\\SourceFiles'
  #获取当前文件夹中的文件名称列表.
  fileList = os.listdir(source_file_dir)
  #如果指定路径下没有要合并的联系人文件，则退出程序.
  if not fileList:
    print("指定路径下没有需要合并的联系人文件.")
    sys.exit(0)                             #退出程序.
  #打开当前目录下的contacts.txt文件，如果没有则创建.
  with open(source_file_dir + '\\contacts.txt','w')  as file:
    tempList = []                           #创建联系人信息列表.
    #遍历文件列表中的联系人文件.
    for fileName in fileList:
      filepath = source_file_dir + '\\' + fileName
      #遍历单个文件，读取1行.
      for line in open(filepath):
        line = re.sub('\n','',line)      #删除联系人信息末尾的’\n’.
        #如果在line不在tempList中，则line没有重复，添加到tempList,并且写入file.
        if line not in tempList and  line + '\n' not in tempList:
          tempList.append(line)           #将1行数据添加到tempList.
          file.write(line)                 #将1行数据写入到file.
          file.write("\n")
    print("合并联系人文件成功！")
except IOError as e:                      #指定路径不存在或读写异常.
    print("异常信息:",e.args[1],e.filename)
except:
  print("合并联系人文件失败！")
