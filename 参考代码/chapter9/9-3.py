with open("Shakespeare.txt","w") as fp:
  num = fp.write( "黑夜无论怎样悠长\n白昼总会到来" )
  print("向文件中写入字符 %d 个！"%(num))
