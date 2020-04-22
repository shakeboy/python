#根据位置格式化.
print('{0}, {1}.'.format('Hello','world'))
print('{}, I am {}.'.format('Hello','Python'))
print('{0} {1}, {1} is a new prgramming language.'.format('Hello','Python'))
#根据key格式化.
print("网站名：{name}, 地址 {url}".format(name="清华大学", url="http://www.tsinghua.edu.cn/"))
#根据字典格式化.
site = {"name": "清华大学", "url": "http://www.tsinghua.edu.cn/"}
print("网站名：{name}, 地址 {url}".format(**site))
#根据列表格式化.
list = ['world','python']
print('hello {names[0]}, I am {names[1]}.'.format(names=list))
print('hello {0[0]},I am {0[1]}.'.format(list))
#数字格式化.
print("{:.2f}".format(3.1415926))     		#2位小数.
print("{:+.2f}".format(3.1415926))    		#带符号.
print("{:.0f}".format(3.1415926))     		#无小数位.
print("{:0>2d}".format(6))            		#填充0.
