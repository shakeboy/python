def func(x, y, z):
    return x * 100 + y * 10 + z
print(func(*[1, 2, 3]))
print(func(**{'z':1, 'y':2, 'x':3}))
print(func(**{'x':1, 'y':2, 'z':3}))
