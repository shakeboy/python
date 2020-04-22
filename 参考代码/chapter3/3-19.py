stockNum = input("请输入您的股票抽签号：")
if stockNum.startswith("88") and stockNum.__len__() == 8: #股票抽签号以88开头且8位.
  print("恭喜您，中签了！")
else:
  pass                    		#pass空语句, 不作任何处理.
