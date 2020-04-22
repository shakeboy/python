import functools
#装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kwargs)
    return wrapper
@log
def tri(a,b,c):
    girth=a+b+c
    print("三角形的周长为：",girth)

@log
def rec(a,b):
    girth = (a + b)*2
    print("矩形的周长为：", girth)

@log
def cyc(r):
    girth=2*3.14*r
    print("圆形的周长为：", girth)

if __name__=="__main__":
    tri(3,4,5)
    print("")
    rec(6,7)
    print("")
    cyc(8)