def addFunc(x, y, *args):
    res = x + y
    for k in args:
        res += k
    return res
print("调用结果:", addFunc(1, 2, 3,4,5,6,7,8,9,10))