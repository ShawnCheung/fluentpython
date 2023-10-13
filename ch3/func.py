import functools


func = lambda x, y: x + y


aa = functools.partial(func, x=10, y=100)
print(aa())