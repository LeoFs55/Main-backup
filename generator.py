#Generator expression, iterables e iterators e generator é uma func que pausa 
iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable)
generator = (n for n in range(1000000))

# for n in generator:
    # print(n)

def geno(min,max):
    while True:
        yield min
        min += 1
        if min>=max:
            return

def g2():
    yield from geno(0,10)
    yield 10
gen = g2()
for i in gen:
    print(i)




