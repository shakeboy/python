# 不带参数的函数
def my_function():
    print("this is my function")


# 调用函数
my_function()


# 带参数的函数
def my_f(a, b):
    return a + b


c = my_f(4, 5)
print(c)


# 默认参数值
def my_f1(name="石义钊"):
    print("我是", name)


my_f1("吴可欣")
my_f1()


# List传参
def my_list(li):  # ambiguous variable name 'l'ambiguous variable name 'l'
    for i in li:
        print(i)


my_list([1, 2, 3, 4])


# 任意参数
# 如果您不知道将传递给您的函数多少个参数，请在函数定义的参数名称前添加 *。
#
# 这样，函数将接收一个参数元组，并可以相应地访问各项：
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Phoebe", "Jennifer", "Rory")


# pass语句
# 函数定义不能为空，但是如果您出于某种原因写了无内容的函数定义，请使用 pass 语句来避免错误。
def my_function():
    pass


# 递归
# Python 也接受函数递归，这意味着定义的函数能够调用自身。
#
# 递归是一种常见的数学和编程概念。它意味着函数调用自身。这样做的好处是可以循环访问数据以达成结果。
#
# 开发人员应该非常小心递归，因为它可以很容易地编写一个永不终止的，或者使用过量内存或处理器能力的函数。但是，在被正确编写后，递归可能是一种非常有效且数学上优雅的编程方法。
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
