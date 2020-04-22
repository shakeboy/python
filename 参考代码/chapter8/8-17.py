import urllib.request,re

with urllib.request.urlopen('http://www.kugou.com/') as file:
  #网页状态.
  print("网页状态:",file.status,file.reason)
  #网页内容.
  data = file.read().decode('utf-8')    	#utf-8字符串解码为unicode字符串.
  #标题.
  reg = '<title>(.*?)</title>'
  title = re.findall(reg,data,re.S|re.M)
  print("标题:",title)
  #关键字.
  reg = '<meta name="keywords" content=.*?>'
  keywords = re.findall(reg,data,re.S|re.M)
  keywordsList = []
  for item in keywords:
    keywordsList = re.findall('content="(.*?)" />',item)
  print("关键字:",keywords)
  #客户端程序下载类型.
  reg = '<div class="download">(.*?)</div>'
  download = re.findall(reg,data,re.S|re.M)
  downloadList = []
  for item in download:
    downloadList = re.findall("<a .*?>(.*?)</a>",item)
  print("客户端程序下载类型:",downloadList)
  #顶级导航.
  reg = '<div class="topNav fr">(.*?)</ul>'
  top_nav = re.findall(reg,data,re.S|re.M)
  top_nav_list = []
  for item in top_nav:
    top_nav_list = re.findall("<a .*?>(.*?)</a>",item)
  print("顶级导航:",top_nav_list)
  #主页导航.
  reg = '<ul class="homeNav">(.*?)</ul>'
  home_nav = re.findall(reg,data,re.S|re.M)
  home_nav_list = []
  for item in home_nav:
    home_nav_list = re.findall("<a .*?>(.*?)</a>",item)
  print("主页导航:",home_nav_list)
  #首页模块.
  reg = '<h3><b>(.*?)</h3>'
  secound_content = re.findall(reg,data,re.S|re.M)
  secound_content_list = []
  for item in secound_content:
    str = re.sub("<.*?>","",item)
    secound_content_list.append(str)
  print("首页模块:",secound_content_list)
