x = 2
assert x >= 0, "x小于0" 	#表达式为True，不触发异常.
x = -2
assert x >= 0, "x小于0" 	#表达式为False，触发异常.
pwd = "e1k4n8"
assert len(pwd) >= 6, "密码字符个数小于6"   	#表达式为True，不触发异常.
pwd = "9k2d3"
assert len(pwd) >= 6, "密码字符个数小于6"   	#表达式为False，抛出异常.
