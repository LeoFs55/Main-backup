def creat_func(func):
    def inside(*args, **kwargs):
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        return result
    return inside

def reverse_string(string):
    return string[::-1]

def is_string(param):
   if not isinstance(param,(str)):
       raise TypeError('Paramentro deve ser um str')
   

validation_reverse_string = creat_func(func=reverse_string)
reverse = validation_reverse_string(string='321')
print(reverse) 