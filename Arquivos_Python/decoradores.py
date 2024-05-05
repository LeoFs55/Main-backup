def creat_func(func):
    def inside(*args, **kwargs):
        print('Decorando...')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print('Decorado.')
        return result
    return inside

@creat_func
def reverse_string(string):
    print(reverse_string.__name__)
    return string[::-1]

def is_string(param):
   if not isinstance(param,(str)):
       raise TypeError('Paramentro deve ser um str')
   

# validation_reverse_string = creat_func(func=reverse_string)
reverse = reverse_string(string='1')
print(reverse) 