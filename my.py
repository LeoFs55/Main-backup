a = [0,2,5,4]
b = [1,2,3,4]
c = []
x = 0
while x < len(a):
    if a[x] != b[x]:
        c.append(a[x])
        c.append(b[x])
    else:
        c.append(a[x])
    x+=1
print(c[:])