def decorator(func):
    print('decorator working')
    def iner(*args, **kwargs):#iner_funcion, iner, nested_funcion ou nested
        print('iner working')
        res = func(*args, **kwargs)
        return res
    return iner

@decorator
def soma(x,y):
    return x+y
