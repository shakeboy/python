a = 100
b = a       						#本质是a把指向100的地址复制给变量b.
print("a的id为:",id(a))         	#输出变量a的引用.
print("b的id为:",id(b))          	#输出变量b的引用.
