# def soma(x,y,/,a,b):
#     return (x+y+a+b)

# print(soma(1,3,a=2,b=3))

def soma(x,y,*,z):
    print(x+y)
soma(1,3,z=2)
